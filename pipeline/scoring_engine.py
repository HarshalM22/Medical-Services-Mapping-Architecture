from .scoring_models import ScoreBreakdown
from sklearn.metrics.pairwise import cosine_similarity
from .anchor_models import MedicalAnchor

import numpy as np

def compute_token_overlap(text_a: str, text_b: str) -> float:
    tokens_a = set(text_a.lower().split())
    tokens_b = set(text_b.lower().split())

    if not tokens_a or not tokens_b:
        return 0.0

    intersection = tokens_a & tokens_b
    union = tokens_a | tokens_b

    return len(intersection) / len(union)

def compute_anchor_overlap(anchor, variant_anchors) -> float:
    """
    anchor: MedicalAnchor extracted from service text
    variant_anchors: precomputed anchors for variant
    """

    score = 0.0
    weight_sum = 0.0

    def overlap(a, b):
        if not a or not b:
            return 0.0
        return len(set(a) & set(b)) / max(len(set(a)), len(set(b)))

    # Body parts (most important)
    score += overlap(anchor.body_part, variant_anchors.body_part) * 0.4
    weight_sum += 0.4

    # Modality
    score += overlap(anchor.modality, variant_anchors.modality) * 0.3
    weight_sum += 0.3

    # Action
    score += overlap(anchor.action, variant_anchors.action) * 0.2
    weight_sum += 0.2

    # Intent (binary)
    if anchor.intent and variant_anchors.intent:
        score += (anchor.intent == variant_anchors.intent) * 0.1
        weight_sum += 0.1

    return score / weight_sum if weight_sum else 0.0
def compute_ontology_depth(
    price_anchor: MedicalAnchor,
    variant_anchor: MedicalAnchor,
) -> float:
    """
    Deeper + more specific matches score higher
    """

    depth = 0.0
    max_depth = 0.0

    # -------------------------
    # Body part specificity
    # -------------------------
    if price_anchor.body_part:
        max_depth += 1

        if variant_anchor.body_part:
            if set(price_anchor.body_part) & set(variant_anchor.body_part):
                # exact overlap
                depth += 1.0
            else:
                # related / parent-level
                depth += 0.6

    # -------------------------
    # Modality specificity
    # -------------------------
    if price_anchor.modality:
        max_depth += 1

        if variant_anchor.modality:
            if set(price_anchor.modality) & set(variant_anchor.modality):
                depth += 1.0
            else:
                depth += 0.5

    return depth / max_depth if max_depth else 0.0

def compute_historical_frequency(variant) -> float:
    """
    usage_count = how often this variant appears historically
    """
    count = variant.get("usage_count", 0)

    # Log scaling to avoid dominance
    if count <= 0:
        return 0.0

    return min(1.0, (count ** 0.5) / 50)

def compute_price_plausibility(variant) -> float:
    price = variant.get("median_price")

    if price is None:
        return 0.5  # neutral if unknown

    if price <= 0:
        return 0.0

    # Hard bounds (tunable)
    if price < 10:
        return 0.2
    if price > 500_000:
        return 0.1

    return 1.0

def compute_penalties(
    price_anchor: MedicalAnchor,
    variant_anchor: MedicalAnchor,
    variant_row,
) -> float:
    penalty = 0.0

    # -------------------------
    # 1. Diagnostic vs Therapeutic conflict
    # -------------------------
    # intent comes from anchors
    # therapeutic flag comes from DB row
    if price_anchor.intent == "diagnostic":
        if "is_therapeutic" in variant_row and variant_row["is_therapeutic"]:
            penalty += 0.3

    # -------------------------
    # 2. Modality conflict
    # -------------------------
    if price_anchor.modality and variant_anchor.modality:
        if not set(price_anchor.modality) & set(variant_anchor.modality):
            penalty += 0.4

    # -------------------------
    # 3. Body part conflict
    # -------------------------
    if price_anchor.body_part and variant_anchor.body_part:
        if not set(price_anchor.body_part) & set(variant_anchor.body_part):
            penalty += 0.5

    return min(1.0, penalty)

def score_variant(
    price_anchor,
    variant_anchor,
    variant_row,
    service_emb,
    variant_emb,
    token_overlap: float,
):
    # 1) anchors
    anchor_overlap = compute_anchor_overlap(price_anchor, variant_anchor)

    # 2) semantic similarity (normalize cosine)
    semantic_score = float(cosine_similarity(service_emb, variant_emb)[0][0])
    semantic_score = (semantic_score + 1.0) / 2.0  # normalize to [0,1]

    anchor_weight = 0.3 + 0.7 * anchor_overlap
    semantic_score = semantic_score * anchor_weight

    # 3) ontology
    ontology_depth = compute_ontology_depth(price_anchor, variant_anchor)

    # 4) other signals
    historical_frequency = compute_historical_frequency(variant_row)
    price_plausibility = compute_price_plausibility(variant_row)

    # 5) penalties
    penalties = compute_penalties(price_anchor, variant_anchor, variant_row)
    penalties = min(penalties, 0.5)

    # 6) SOFT coupling: anchors affect semantic, not kill it
    semantic_score = semantic_score * (0.3 + 0.7 * anchor_overlap)

    return ScoreBreakdown(
        semantic_score=semantic_score,
        anchor_overlap=anchor_overlap,
        token_overlap=token_overlap,
        ontology_depth=ontology_depth,
        historical_frequency=historical_frequency,
        price_plausibility=price_plausibility,
        penalties=penalties,
    )