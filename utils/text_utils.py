def token_overlap(a: str, b: str) -> float:
    return len(set(a.split()) & set(b.split()))