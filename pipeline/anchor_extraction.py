from .ontology_data import BODY_PARTS, MODALITIES, ACTIONS, INTENT_KEYWORDS
from .anchor_models import MedicalAnchor



def extract_anchors(tokens: list[str]) -> MedicalAnchor:
    """
    Optimized:
    - Separates primary vs secondary anchors
    - Phrase-aware (cheap)
    - Deterministic ordering
    """

    token_set = set(tokens)

    body = [b for b in BODY_PARTS if b in token_set]
    modality = [m for m in MODALITIES if m in token_set]

 
    action = [a for a in ACTIONS if a in token_set][:2]

    intent = None
    for k, words in INTENT_KEYWORDS.items():
        if token_set.intersection(words):
            intent = k
            break


    approach = "flexible" if "flexible" in token_set else None

    return MedicalAnchor(
        body_part=body,
        modality=modality,
        action=action,
        approach=approach,
        intent=intent,
    )