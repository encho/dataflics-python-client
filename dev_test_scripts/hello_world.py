import dataflics


DATAFLICS_BASE_URL = "http://localhost:3000"

print(dataflics)

# Configure the library with your API endpoint (and API key if needed)
dataflics.configure(DATAFLICS_BASE_URL, api_key="YOUR_API_KEY")

# Create a new video object
new_video = dataflics.create_video(
    "My New Video Name",
    {"screen": "somescreenId", "palette": "somePaletteId", "typography": "someTypographyId"}
)

print(new_video)


# Save (i.e. send a POST to your REST API behind the scenes)
new_video.save()
