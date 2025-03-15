from dataclasses import dataclass, field

@dataclass
class Title01:
    # The slide type is fixed to "title-01"
    type: str = field(init=False, default="title-01")
    title: str
    durationInFrames: int
