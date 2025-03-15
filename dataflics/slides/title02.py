from dataclasses import dataclass, field

@dataclass
class Title02:
    # The slide type is fixed to "title-02"
    type: str = field(init=False, default="title-02")
    title: str
    subtitle: str
    durationInFrames: int
