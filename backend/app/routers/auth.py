from fastapi import APIRouter, Query
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from ..config import settings
from ..auth import get_access_token


router = APIRouter()

@router.get("/login")
def login():
    # Construir la URL de autorización de Strava
    strava_auth_url = (
        f"https://www.strava.com/oauth/authorize?"
        f"client_id={settings.STRAVA_CLIENT_ID}&"
        f"redirect_uri={settings.STRAVA_REDIRECT_URI}&"
        f"response_type=code&"
        f"scope=activity:read"
    )
    print(strava_auth_url)
    return RedirectResponse(url=strava_auth_url)



@router.get("/callback")
def auth_callback(code: str = Query(...)):
    # Intercambiar el código por un token de acceso
    token = get_access_token(code)

    if not token:
        return {"error": "Failed to retrieve access token"}

    # Construir la URL para redirigir al frontend con el token
    redirect_url = f"/?token={token}"
    return RedirectResponse(url=redirect_url)