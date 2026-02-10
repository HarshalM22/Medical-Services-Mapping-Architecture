from .normalization import normalize
from .ontology_resolution import resolve_terms
from .anchor_extraction import extract_anchors


def prune_candidates(price_anchor, variants, max_candidates=40):
    """
    Optimized pruning:
    - Fail-fast hard gates
    - Adaptive scoring
    - No expensive ops
    """

    scored = []

    for variant in variants:
        variant_text = f"{variant['variant_name']} : {variant['variant_description']}"
        tokens = resolve_terms(normalize(variant_text))
        variant_anchor = extract_anchors(tokens)

        if variant_anchor.is_empty():
            continue

        # -------------------------
        # HARD GATES (FAIL FAST)
        # -------------------------
        if price_anchor.modality and variant_anchor.modality:
            if not set(price_anchor.modality) & set(variant_anchor.modality):
                continue

        if price_anchor.body_part and variant_anchor.body_part:
            if not set(price_anchor.body_part) & set(variant_anchor.body_part):
                continue

        # -------------------------
        # SOFT SCORING
        # -------------------------
        score = 0.0

        # Primary anchors
        score += 0.45 * bool(
            set(price_anchor.body_part) & set(variant_anchor.body_part)
        )
        score += 0.35 * bool(
            set(price_anchor.modality) & set(variant_anchor.modality)
        )

        # Secondary anchors
        score += 0.10 * bool(
            set(price_anchor.action) & set(variant_anchor.action)
        )

        if price_anchor.intent and variant_anchor.intent:
            score += 0.10 * (price_anchor.intent == variant_anchor.intent)

        # Fail weak candidates early
        if score < 0.4:
            continue

        scored.append((
            score,
            {
                "row": variant,
                "anchors": variant_anchor,
                "text": variant_text,
            }
        ))

    if not scored:
        return []

    scored.sort(key=lambda x: x[0], reverse=True)
    return [v for _, v in scored[:max_candidates]]