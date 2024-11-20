import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

class Settings:
    STRAVA_CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
    STRAVA_CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")
    STRAVA_REDIRECT_URI = os.getenv("STRAVA_REDIRECT_URI")
    STRAVA_API_BASE_URL = "https://www.strava.com/api/v3"

settings = Settings()
