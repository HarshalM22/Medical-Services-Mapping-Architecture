
import json
import numpy as np

from .embedding_generator import (
    generate_embeddings,
)
from .normalization import normalize
from .db_operations import DBAdapter


DEFAULT_EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
VARIANT_EMBED_BATCH = 512




def build_variant_text(row: dict) -> str:
    name = (row.get("variant_name") or "").strip()
    desc = (row.get("variant_description") or "").strip()

    # name is mandatory in your schema
    if desc:
        return normalize(f"{name}:{desc}")
    return normalize(f"{name}:{desc}")


def ensure_variant_embeddings( expected_model: str = DEFAULT_EMBED_MODEL):
    """
    Ensures every procedure_variant has an embedding stored in DB.
    Returns:
        variant_embeddings: dict[int, np.ndarray]
    """
    db=DBAdapter()

    variants = db.load_procedure_variants_with_embeddings()

    missing = []
    for v in variants:
        emb_json = v.get("embedding_json")
        emb_model = v.get("embedding_model")

        # Missing OR model mismatch → regenerate
        if not emb_json or emb_model != expected_model:
            missing.append(v)

    print(f"[Variants] total={len(variants)} missing_or_mismatch={len(missing)}")

    # -----------------------------
    # Backfill missing embeddings
    # -----------------------------
    if missing:
        updates = []

        for i in range(0, len(missing), VARIANT_EMBED_BATCH):
            batch = missing[i : i + VARIANT_EMBED_BATCH]
            texts = [build_variant_text(v) for v in batch]

            embs = generate_embeddings(texts, batch_size=VARIANT_EMBED_BATCH)

            for v, emb in zip(batch, embs):
                emb = np.asarray(emb, dtype=np.float32)
                updates.append(
                    {
                        "id": v["id"],
                        "embedding_json": json.dumps(emb.tolist()),
                        "embedding_dim": int(emb.shape[0]),
                        "embedding_model": expected_model,
                    }
                )

        db.bulk_update_variant_embeddings(updates)
        print(f"[Variants] stored {len(updates)} embeddings")

        # reload updated rows
        variants = db.load_procedure_variants_with_embeddings()

    # -----------------------------
    # Build in-memory cache
    # -----------------------------
    variant_embeddings = {}

    for v in variants:
        emb_json = v.get("embedding_json")
        if not emb_json:
            continue

        emb = np.asarray(json.loads(emb_json), dtype=np.float32)
        variant_embeddings[v["id"]] = emb

    print(f"[Variants] cache ready: {len(variant_embeddings)} embeddings loaded")

    return variants, variant_embeddings