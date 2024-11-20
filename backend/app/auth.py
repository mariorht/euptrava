import requests
from .config import settings

def get_access_token(code: str):
    response = requests.post(
        "https://www.strava.com/oauth/token",
        data={
            "client_id": settings.STRAVA_CLIENT_ID,
            "client_secret": settings.STRAVA_CLIENT_SECRET,
            "code": code,
            "grant_type": "authorization_code"
        }
    )
    return response.json().get("access_token")

