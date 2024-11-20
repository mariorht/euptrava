from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers.auth import router as auth_router
from app.routers.activities import router as activities_router

app = FastAPI()

# Registrar routers
app.include_router(auth_router, prefix="/auth")
app.include_router(activities_router, prefix="/api")

# Servir archivos estáticos
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")



@app.on_event("startup")
async def log_routes():
    for route in app.routes:
        print(f"Ruta: {route.path} -> {route.name}")
