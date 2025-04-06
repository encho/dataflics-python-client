from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class Title02:
    type: str = field(init=False, default="title-02")
    title: str
    subtitle: str
    durationInFrames: int

    def serialize(self) -> Dict[str, Any]:
        return {
            "type": self.type,
            "title": self.title,
            "subtitle": self.subtitle,
            "durationInFrames": self.durationInFrames,
        }
