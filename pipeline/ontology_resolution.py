from .ontology_data import SYNONYMS

def resolve_terms(text: str) -> list[str]:
    tokens = text.split()
    resolved = []
    for t in tokens:
        resolved.append(SYNONYMS.get(t, t))
    return resolved