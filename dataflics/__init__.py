# dataflics/__init__.py
from typing import Optional
from .client import Client
from .video import Video

# A module-level variable to hold the default client instance
_default_client: Optional[Client] = None

def configure(base_url: str, api_key: Optional[str] = None) -> None:
    """
    Configure the library with the API base URL and an optional API key.
    """
    global _default_client
    _default_client = Client(base_url, api_key)

def create_video(name: str, colorPalette: str, typography: str, screen: str) -> Video:
    """
    Create a video using the configured client.
    """
    if _default_client is None:
        raise Exception("Client not configured. Call dataflics.configure() first.")
    return _default_client.create_video(name, colorPalette, typography, screen)
