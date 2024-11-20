# EUPTrava

**EUPTrava** es una aplicación web desarrollada con FastAPI que permite ver el histórico de actividades de Strava y comparar rutas y segmentos con amigos.

## Estructura del Proyecto

```plaintext
EUPTrava/
├── backend/
│   ├── app/
│   │   ├── main.py           # Punto de entrada de FastAPI
│   │   ├── config.py         # Configuración de API de Strava
│   │   ├── auth.py           # Autenticación OAuth2 para Strava
│   │   ├── models.py         # Modelos de datos (puede estar vacío)
│   │   ├── routers/
│   │   │   ├── activities.py # Rutas para obtener actividades de Strava
│   │   │   └── __init__.py   # Inicialización de paquete (puede estar vacío)
│   │   └── static/
│   │       ├── index.html    # Interfaz HTML
│   │       └── scripts.js    # JavaScript para manejar el frontend
│   ├── Dockerfile            # Configuración de Docker para el backend
│   └── requirements.txt      # Dependencias de Python
├── setup_env.sh              # Script para configurar entorno virtual y lanzar servidor
└── docker-compose.yml        # Configuración de Docker Compose para contenedores
```

## Configuración

### Uso de entorno virtual (sin Docker)

1. **Requisitos previos:**
   - Asegúrate de tener instalado Python 3.9 o superior.
   - Crea un archivo `.env` con las variables necesarias para la API de Strava:

     ```plaintext
     STRAVA_CLIENT_ID=tu_client_id
     STRAVA_CLIENT_SECRET=tu_client_secret
     STRAVA_REDIRECT_URI=http://localhost:8000/redirect
     ```

2. **Ejecutar el script de configuración:**

   Desde la raíz del proyecto, ejecuta el siguiente comando:

   ```bash
   ./setup_env.sh
   ```

   Este script:
   - Crea y configura un entorno virtual en la carpeta `venv`.
   - Instala las dependencias especificadas en `backend/requirements.txt`.
   - Lanza el servidor local en `http://127.0.0.1:8000`.

3. **Acceso a la aplicación:**

   Abre tu navegador en `http://127.0.0.1:8000` para acceder a la interfaz.

4. **Detener el servidor:**
   - Pulsa `Ctrl + C` en la terminal para detener el servidor.

### Uso con Docker

1. **Configuración previa:**
   - Asegúrate de tener Docker y Docker Compose instalados.
   - Crea un archivo `.env` con las variables necesarias para la API de Strava (igual que en el paso anterior).

2. **Construir y lanzar el proyecto:**

   Ejecuta el siguiente comando para construir y lanzar el proyecto con Docker Compose:

   ```bash
   docker-compose up --build
   ```

3. **Acceso a la aplicación:**

   Abre tu navegador en `http://localhost:8000` para acceder a la interfaz.

4. **Detener el proyecto:**

   ```bash
   docker-compose down
   ```

## Notas Adicionales

- Si usas el entorno virtual, recuerda activarlo cada vez que trabajes en el proyecto:
  ```bash
  source venv/bin/activate
  ```
- Para salir del entorno virtual, usa:
  ```bash
  deactivate
  ```

## Tecnologías Utilizadas

- **Backend:** FastAPI
- **Frontend:** HTML, JavaScript (sirviéndose directamente desde el backend)
- **Autenticación:** OAuth2 para Strava
- **Contenedorización:** Docker y Docker Compose (opcional)

