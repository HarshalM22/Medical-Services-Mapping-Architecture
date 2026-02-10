from dataclasses import dataclass

@dataclass
class ScoreBreakdown:
    semantic_score: float
    anchor_overlap: float
    token_overlap: float
    ontology_depth: float
    historical_frequency: float
    price_plausibility: float
    penalties: float

    @staticmethod
    def zero():
        return ScoreBreakdown(
            semantic_score=0.0,
            anchor_overlap=0.0,
            token_overlap=0.0,
            ontology_depth=0.0,
            historical_frequency=0.0,
            price_plausibility=0.0,
            penalties=0.0,
        )

    def final_score(self) -> float:
        raw = (
            self.semantic_score
            + self.anchor_overlap
            + self.token_overlap
            + self.ontology_depth
            + self.historical_frequency
            + self.price_plausibility
            - self.penalties
        )
        return max(0.0, min(1.0, raw))