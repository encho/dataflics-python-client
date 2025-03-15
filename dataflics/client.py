# dataflics/client.py
import requests
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .video import Video  # Only imported for type checking

class Client:
    def __init__(self, base_url: str, api_key: Optional[str] = None) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key

    def create_video(self, name: str, colorPalette: str, typography: str, screen: str) -> "Video":
        """
        Create a new Video instance with the provided parameters.
        """
        from .video import Video  # Lazy import to avoid circular dependencies
        return Video(
            name=name,
            colorPalette=colorPalette,
            typography=typography,
            screen=screen
        )

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

    def get(self, endpoint: str) -> Dict[str, Any]:
        """
        Helper method to send a GET request to the API.
        """
        url = f"{self.base_url}{endpoint}"
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
