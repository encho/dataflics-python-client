# dataflics/video.py
from typing import TypedDict
from .client import Client

class VideoOptions(TypedDict):
    screen: str
    palette: str
    typography: str

class Video:
    def __init__(self, name: str, options: VideoOptions, client: Client) -> None:
        self.name: str = name
        self.options: VideoOptions = options
        self.client: Client = client
        # You might store additional information returned from the API here
        self.id = None

    def save(self) -> "Video":
        """
        Sends a POST request to create the video.
        """
        payload = {
            "name": self.name,
            "screenId": self.options.get("screen"),
            "colorPaletteId": self.options.get("palette"),
            "typographyId": self.options.get("typography"),
        }
        response = self.client.post("/api/videos", payload)
        # Optionally, update the video object with response data
        for key, value in response.items():
            setattr(self, key, value)
        return self
