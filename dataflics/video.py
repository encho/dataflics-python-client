# dataflics/video.py
import json
from typing import TypedDict, Any, Dict
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
        Sends a POST request to create the video, logs the full response data to the console,
        then GETs the rich video details from the API and logs them in humanly readable formatting.
        """
        payload = {
            "name": self.name,
            "screenId": self.options.get("screen"),
            "colorPaletteId": self.options.get("palette"),
            "typographyId": self.options.get("typography"),
        }
        response = self.client.post("/api/videos", payload)
        # Log the full response data from the POST call.
        print("API Response:", response)
        # Update the video object with response data (such as the video id).
        for key, value in response.items():
            setattr(self, key, value)
        
        # Now, fetch the rich video details using a GET request.
        # rich_video = self.client.get(f"/api/videos/{self.id}")
        rich_video: Dict[str, Any] = self.client.get(f"/api/videos/{self.id}")

        # Log the rich video details in a humanly readable (pretty-printed) format.
        print("Rich Video:")
        print(json.dumps(rich_video, indent=2))
        
        return self
