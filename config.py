class Config:
    APOD_API_KEY = "HX0IGnZXQcGmjF8D0PkgOfk0aduJ3qBq6m27286b"
    
    NEO_API_KEY = "QcTRnH6ssd7CUM4rGn4GSgMeq5fQiBzEO8EaQKOm"
    NEO_API_START_DATE = "20230101"
    NEO_API_END_DATE = "20240105"
    NEO_API_ENDPOINT = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={NEO_API_START_DATE}&end_date={NEO_API_END_DATE}&api_key={NEO_API_KEY}"
    
    import os


    # Define the URI for your PostgreSQL database
    SQLALCHEMY_DATABASE_URI ='postgresql://postgres:Magic323!@localhost:5432/spaceuser'
