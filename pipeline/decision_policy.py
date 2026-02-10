def decide(score: float) -> str:
    if score >= 0.90:
        return "AUTO_MAP"
    if score >= 0.75:
        return "PROBABLE"
    if score >= 0.60:
        return "REVIEW"
    return "REJECT"