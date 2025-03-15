from dataclasses import dataclass, field
from typing import List, Union

from  slides.title01 import Title01
from  slides.title02 import Title02

# Define a type alias for valid slide types
Slide = Union[Title01, Title02]

@dataclass
class VideoNew:
    name: str
    colorPalette: str
    typography: str
    screen: str
    slides: List[Slide] = field(default_factory=list)
    
    def addSlide(self, slide: Slide) -> None:
        self.slides.append(slide)

# Example script demonstrating instantiation and usage
if __name__ == "__main__":
    # Instantiate a VideoNew object
    video = VideoNew(
        name="My Awesome Video",
        colorPalette="defaultPalette",
        typography="defaultTypography",
        screen="defaultScreen"
    )
    
    # Create two slide objects
    slide1 = Title01(
        title="Welcome to the Show",
        durationInFrames=120
    )
    
    slide2 = Title02(
        title="Introduction",
        subtitle="A brief overview",
        durationInFrames=150
    )
    
    # Add the slides to the video
    video.addSlide(slide1)
    video.addSlide(slide2)
    
    # Print out the video object
    print(video)
