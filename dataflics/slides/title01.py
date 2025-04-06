from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class Title01:
    type: str = field(init=False, default="title-01")
    title: str
    durationInFrames: int

    def serialize(self) -> Dict[str, Any]:
        return {
            "type": self.type,
            "title": self.title,
            "durationInFrames": self.durationInFrames,
        }
