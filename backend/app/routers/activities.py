from fastapi import APIRouter, HTTPException, Query
import requests
from ..config import settings

router = APIRouter()

@router.get("/activities")
async def get_activities(token: str = Query(...)):
    # Validar el token recibido
    if not token:
        raise HTTPException(status_code=400, detail="Token is missing")

    # Llamar a la API de Strava con el token
    response = requests.get(
        f"{settings.STRAVA_API_BASE_URL}/athlete/activities",
        headers={"Authorization": f"Bearer {token}"}
    )

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching activities from Strava")
    
    # Devolver las actividades obtenidas de Strava
    return response.json()