# dataflics/video.py
from dataclasses import dataclass, field
from typing import List, Union, Any, Dict, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .client import Client

from .slides.title01 import Title01
from .slides.title02 import Title02
from .slides.barchart01 import Barchart01

# Define a type alias for valid slide types
Slide = Union[Title01, Title02, Barchart01]

@dataclass
class Video:
    name: str
    colorPalette: str
    typography: str
    screen: str
    fps: int
    client: "Client" = field(repr=False)
    slides: List[Slide] = field(default_factory=list)
    id: Optional[str] = field(init=False, default=None)  # Will be set after saving

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
        print(f"FPS           : {self.fps}")
        print("Slides:")
        if not self.slides:
            print("  No slides available.")
        else:
            for idx, slide in enumerate(self.slides, start=1):
                print(f"  Slide {idx}:")
                print(f"    {slide}")

    def save(self) -> "Video":
        payload: Dict[str, Any] = {
            "name": self.name,
            "screen": self.screen,
            "colorPalette": self.colorPalette,
            "typography": self.typography,
            "fps": self.fps,
            "slides": [slide.serialize() for slide in self.slides],
        }
        print("Payload to be sent to API backend:")
        print(payload)

        response = self.client.post("/api/videos", payload)

        print("********")
        print("API Response:", response)
        print(self.client.base_url)
        print(response)
        print("********")

        self.id = str(response)

        return self


    @property
    def url(self) -> Optional[str]:
        """
        Returns the URL to access the created video.
        If the video hasn't been saved (id is None), returns None.
        """
        if self.id is None:
            return None
        return f"{self.client.base_url}/app/videos/{self.id}"

# Example script demonstrating instantiation and usage
if __name__ == "__main__":
    from .client import Client
    # Create a dummy client for demonstration purposes.
    dummy_client = Client("http://localhost:3000", api_key="YOUR_API_KEY")
    
    # Instantiate a Video object with the dummy client.
    video = Video(
        name="My Awesome Video",
        colorPalette="defaultPalette",
        typography="defaultTypography",
        screen="defaultScreen",
        fps=30,
        client=dummy_client
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
    
    # Save the video, which posts to the API and prints the responses
    video.save()

    # Access the computed URL property
    print("Video URL:", video.url)
