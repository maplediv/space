class Config:
    APOD_API_KEY = "HX0IGnZXQcGmjF8D0PkgOfk0aduJ3qBq6m27286b"
    MARS_API_KEY = "HX0IGnZXQcGmjF8D0PkgOfk0aduJ3qBq6m27286b"
    MARS_API_ENDPOINT = f"https://api.nasa.gov/insight_weather/?api_key={MARS_API_KEY}&feedtype=json&ver=1.0"
    ROVER_API_KEY = "QcTRnH6ssd7CUM4rGn4GSgMeq5fQiBzEO8EaQKOm"  # Replace with your actual Rover API key
    ROVER_API_ENDPOINT = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    NEO_API_KEY = "QcTRnH6ssd7CUM4rGn4GSgMeq5fQiBzEO8EaQKOm"
    NEO_API_START_DATE = "20230101"
    NEO_API_END_DATE = "20240105"
    NEO_API_ENDPOINT = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={NEO_API_START_DATE}&end_date={NEO_API_END_DATE}&api_key={NEO_API_KEY}"
    EPIC_API_KEY = "HX0IGnZXQcGmjF8D0PkgOfk0aduJ3qBq6m27286b"  # Replace with your actual EPIC API key
    EPIC_API_BASE_URL = "https://epic.gsfc.nasa.gov/api/natural"
    INSIGHT_API_KEY = "QcTRnH6ssd7CUM4rGn4GSgMeq5fQiBzEO8EaQKOm"  # Replace with your actual InSight API key
    INSIGHT_API_ENDPOINT = f"https://api.nasa.gov/insight_weather/?api_key={INSIGHT_API_KEY}&feedtype=json&ver=1.0"
    JWST_API_KEY = "6a9e807e-7d50-4a7d-8fba-edd4b5073d91"  # Replace with your actual JWST API key
    JWST_API_BASE_URL = "https://api.jwstapi.com"
