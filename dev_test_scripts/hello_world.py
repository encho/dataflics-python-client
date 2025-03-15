import uuid
import dataflics

DATAFLICS_BASE_URL = "http://localhost:3000"

# Configure the library with your API endpoint (and API key if needed)
dataflics.configure(DATAFLICS_BASE_URL, api_key="YOUR_API_KEY")


def generate_unique_video_name():
    """
    Generates a unique video name using a shortened UUID.
    
    Returns:
        str: A unique video name in the format 'video_<short_id>.mp4'
    """
    # Generate a random unique hex string and take only the first 8 characters.
    short_id = uuid.uuid4().hex[:8]
    return f"video_{short_id}.mp4"


video_name = generate_unique_video_name()

# Create a new video object
new_video = dataflics.create_video(
    video_name,
    {"screen": "screen:08ppk772i6hkhlshdygh",
      "palette": "colorPalette:fmomzlqk53ufabsq1vjt",
      "typography": "typography:bl5iye1yw2uw2xg2eefn"}
)

print(new_video)

# Save (i.e. send a POST to your REST API behind the scenes)
new_video.save()
