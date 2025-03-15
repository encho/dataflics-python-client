from dataclasses import dataclass, field
from typing import List, Union

from .slides.title01 import Title01
from .slides.title02 import Title02

# Define a type alias for valid slide types
Slide = Union[Title01, Title02]

@dataclass
class Video:
    name: str
    colorPalette: str
    typography: str
    screen: str
    slides: List[Slide] = field(default_factory=list)
    
    def addSlide(self, slide: Slide) -> None:
        self.slides.append(slide)
    
    def pretty_print(self) -> None:
        """Prints the video details in a humanly readable format."""
        print("Video Details:")
        print("--------------")
        print(f"Name          : {self.name}")
        print(f"Color Palette : {self.colorPalette}")
        print(f"Typography    : {self.typography}")
        print(f"Screen        : {self.screen}")
        print("Slides:")
        if not self.slides:
            print("  No slides available.")
        else:
            for idx, slide in enumerate(self.slides, start=1):
                print(f"  Slide {idx}:")
                # Check if the slide has its own pretty_print method.
                # if hasattr(slide, "pretty_print") and callable(slide.pretty_print):
                #     slide.pretty_print(indent=4)
                # else:
                #     print(f"    {slide}")
                print(f"    {slide}")

# Example script demonstrating instantiation and usage
if __name__ == "__main__":
    # Instantiate a Video object
    video = Video(
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
    
    # Print out the video object in a human-friendly format
    video.pretty_print()
