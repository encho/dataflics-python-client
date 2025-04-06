from dataclasses import dataclass, field
from typing import List

@dataclass
class BarChart01Item:
    id: str
    label: str
    value: float

@dataclass
class BarChart01:
    # The slide type is fixed to "barchart-01"
    type: str = field(init=False, default="barchart-01")
    title: str
    durationInFrames: int
    data: List[BarChart01Item]