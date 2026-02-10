from queue import Queue
import json
import math
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
from threading import Thread

from .db_operations import DBAdapter
from .embedding_generator import (
    generate_embeddings,
    prepare_embedding_row,
)
from .variant_embedding_cache import (
    ensure_variant_embeddings,
    DEFAULT_EMBED_MODEL,
)
from .normalization import normalize
from .ontology_resolution import resolve_terms
from .anchor_extraction import extract_anchors
from .candidate_pruning import prune_candidates
from .scoring_engine import score_variant
from .decision_policy import decide


# ======================================================
# CONFIG (TUNE BASED ON HARDWARE)
# ======================================================
ITEM_CHUNK_SIZE = 5000
EMBED_BATCH_SIZE = 512
SCORING_THREADS = 8
MAX_CANDIDATES = 30

QUEUE_MAXSIZE = 200

# ======================================================
# UTILS
# ======================================================
def compute_token_overlap(service_tokens, variant_text):
    variant_tokens = set(resolve_terms(normalize(variant_text)))
    if not service_tokens or not variant_tokens:
        return 0.0
    return len(service_tokens & variant_tokens) / max(
        len(service_tokens), len(variant_tokens)
    )


def sanitize_embedding_rows(rows):
    for r in rows:
        for k in ("embedding", "variant_embedding"):
            v = r.get(k)
            if v is not None and hasattr(v, "tolist"):
                r[k] = json.dumps(v.tolist())
    return rows




def candidate_worker(price_items, variants, out_queue):
    print("getting all the candidates")

    total = 0
    skipped_no_text = 0
    skipped_no_anchors = 0
    skipped_no_candidates = 0
    pushed = 0

    for item in price_items:
        total += 1

        raw_text = item.get("service_description")
        if not raw_text:
            skipped_no_text += 1
            continue

        normalized = normalize(raw_text)
        service_tokens = set(resolve_terms(normalized))
        anchors = extract_anchors(service_tokens)

        if anchors.is_empty():
            skipped_no_anchors += 1
            continue

        candidates = prune_candidates(
            anchors,
            variants,
            max_candidates=MAX_CANDIDATES,
        )
        if not candidates:
            skipped_no_candidates += 1
            continue

        pushed += 1
        out_queue.put({
            "item": item,
            "normalized": normalized,
            "service_tokens": service_tokens,
            "anchors": anchors,
            "candidates": candidates,
        })

    print(
        f"[CandidateWorker] total={total} pushed={pushed} "
        f"no_text={skipped_no_text} no_anchors={skipped_no_anchors} no_candidates={skipped_no_candidates}"
    )

    # IMPORTANT: q1 is consumed by ONLY ONE embedding_worker
    out_queue.put(None)

# ======================================================
# PHASE 2 — SERVICE EMBEDDING (GPU)
# ======================================================
def embedding_worker(in_queue, out_queue):
    print("Into Embeddings")
    buffer = []

    while True:
        item = in_queue.get()
        if item is None:
            break

        buffer.append(item)

        if len(buffer) >= EMBED_BATCH_SIZE:
            texts = [b["normalized"] for b in buffer]
            embs = generate_embeddings(texts, EMBED_BATCH_SIZE)

            for b, emb in zip(buffer, embs):
                b["service_emb"] = emb.reshape(1, -1)
                out_queue.put(b)

            buffer.clear()

    # flush
    if buffer:
        texts = [b["normalized"] for b in buffer]
        embs = generate_embeddings(texts, EMBED_BATCH_SIZE)
        for b, emb in zip(buffer, embs):
            b["service_emb"] = emb.reshape(1, -1)
            out_queue.put(b)

    for _ in range(SCORING_THREADS):
        out_queue.put(None)


# ======================================================
# PHASE 3 — SCORING + DECISION (CPU)
# ======================================================
def scoring_worker(in_queue, variant_embeddings, rows_out):
    print("Phase 3 started : scoring")
    while True:
        ctx = in_queue.get()
        if ctx is None:
            break

        best = None
        best_score = 0.0

        for c in ctx["candidates"]:
            variant_id = c["row"].id
            variant_emb = variant_embeddings.get(variant_id)

            if variant_emb is None:
                continue

            token_overlap = compute_token_overlap(
                ctx["service_tokens"],
                c["text"],
            )

            score_obj = score_variant(
                price_anchor=ctx["anchors"],
                variant_anchor=c["anchors"],
                variant_row=c["row"],
                service_emb=ctx["service_emb"],
                variant_emb=variant_emb.reshape(1, -1),
                token_overlap=token_overlap,
            )

            score = score_obj.final_score()

            if score > best_score:
                best_score = score
                best = (c, variant_emb)

        decision = decide(best_score)

        if not best:
            continue

        if decision == "REJECT":
            continue

        candidate, variant_emb = best

        row = prepare_embedding_row(
            ctx["item"],
            candidate["row"],
            ctx["service_emb"],
            variant_emb,
        )

        rows_out.append(row)


# ======================================================
# MAIN RUNNER
# ======================================================
def run_mrf_mapping():
    db = DBAdapter()

    # Load variants + ensure embeddings exist (dynamic + optimal)
    variants, variant_embeddings = ensure_variant_embeddings(
        expected_model=DEFAULT_EMBED_MODEL,
    )

    price_items = db.load_price_items()
    total = len(price_items)
    print(f"Processing {total} items")

    for i in range(0, total, ITEM_CHUNK_SIZE):
        chunk = price_items[i : i + ITEM_CHUNK_SIZE]
        print(f"Chunk {i} → {i + len(chunk)}")

        q1 = Queue(maxsize=QUEUE_MAXSIZE)
        q2 = Queue(maxsize=QUEUE_MAXSIZE)

        # Thread-safe output collector
        rows_out = Queue()

        t1 = Thread(target=candidate_worker, args=(chunk, variants, q1))
        t2 = Thread(target=embedding_worker, args=(q1, q2))

        t1.start()
        t2.start()

        # Start multiple scoring threads
        scoring_threads = []
        for _ in range(SCORING_THREADS):
            t = Thread(
                target=scoring_worker,
                args=(q2, variant_embeddings, rows_out),
            )
            t.start()
            scoring_threads.append(t)

        t1.join()
        t2.join()

        for t in scoring_threads:
            t.join()

        # Collect rows from queue
        rows_to_insert = []
        while not rows_out.empty():
            rows_to_insert.append(rows_out.get())
        
        print(f"length of inserting ROW's is {len(rows_to_insert)}") 
        db.save_embeddings(
            sanitize_embedding_rows(rows_to_insert)
        )

    print("DONE")

if __name__ == "__main__":
    run_mrf_mapping()