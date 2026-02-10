from dataclasses import dataclass ,field
from typing import List, Optional

@dataclass(frozen=True)
class MedicalAnchor:
    body_part: List[str] = field(default_factory=list)
    modality: List[str] = field(default_factory=list)
    action: List[str] = field(default_factory=list)
    approach: Optional[str] = None
    intent: Optional[str] = None

    def is_empty(self) -> bool:
        return not (
            self.body_part
            or self.modality
            or self.action
            or self.approach
            or self.intent
        )