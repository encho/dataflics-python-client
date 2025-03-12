# dataflics/client.py
import requests
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .video import Video, VideoOptions  # Only imported for type checking

class Client:
    def __init__(self, base_url: str, api_key: Optional[str] = None) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key

    def create_video(self, name: str, options: "VideoOptions") -> "Video":
        """
        Create a new Video instance.
        """
        # Importing Video here lazily avoids a circular import at the module level
        from .video import Video
        return Video(name, options, self)

    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Helper method to send a POST request to the API.
        """
        url = f"{self.base_url}{endpoint}"
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
