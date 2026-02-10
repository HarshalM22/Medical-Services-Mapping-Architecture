import re
from .ontology_data import ABBREVIATIONS

def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)

    for abbr, expanded in ABBREVIATIONS.items():
        text = re.sub(rf"\b{abbr}\b", expanded, text)

    text = re.sub(r"\s+", " ", text).strip()
    return text