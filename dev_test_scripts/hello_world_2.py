import uuid
from datetime import datetime
import dataflics

DATAFLICS_BASE_URL = "http://localhost:3000"

# Configure the library with your API endpoint (and API key if needed)
dataflics.configure(DATAFLICS_BASE_URL, api_key="YOUR_API_KEY")


def generate_unique_video_name() -> str:
    """
    Generates a unique video name using a shortened UUID.
    
    Returns:
        str: A unique video name in the format 'video_<short_id>'
    """
    short_id = uuid.uuid4().hex[:8]
    return f"video_{short_id}"


video_name = generate_unique_video_name()

# Create a new video object using Video with direct parameters
new_video = dataflics.create_video(
    video_name,
    fps=30,
    colorPalette="colorPalette:1xm9wtr14x2pyrovb797",
    typography="typography:bl5iye1yw2uw2xg2eefn",
    screen="screen:08ppk772i6hkhlshdygh"
)

# Create slides in a type-safe manner using the re-exported classes

# Instead of a hardcoded title, we display the current date and time.
current_dt_str = datetime.now().strftime("%Y-%m-%d %H:%M")
title_01_slide = dataflics.Title01(
    title=current_dt_str,
    durationInFrames=120
)

title_02_slide = dataflics.Title02(
    title="Introduction",
    subtitle="A brief overview",
    durationInFrames=150
)

title_02_slide_again = dataflics.Title02(
    title="Introduction 2",
    subtitle="A brief overview",
    durationInFrames=150
)

# Add the slides to the video
new_video.addSlide(title_01_slide)
new_video.addSlide(title_02_slide)
new_video.addSlide(title_02_slide_again)

# Pretty print the video object along with its slides
new_video.pretty_print()

new_video.save()

# Access the computed URL property
print("Video URL:", new_video.url)

# new_video.render()
