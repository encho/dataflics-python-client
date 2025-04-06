from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class Barchart01Item:
    id: str
    label: str
    value: float

    def serialize(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "label": self.label,
            "value": self.value,
        }

@dataclass
class Barchart01:
    type: str = field(init=False, default="barchart-01")
    title: str
    durationInFrames: int
    data: List[Barchart01Item]

    def serialize(self) -> Dict[str, Any]:
        return {
            "type": self.type,
            "title": self.title,
            "durationInFrames": self.durationInFrames,
            "data": [item.serialize() for item in self.data],
        }
