#!/bin/bash

# Nombre del entorno virtual
VENV_DIR="venv"


# Activar el entorno virtual
echo "Activando entorno virtual..."
source $VENV_DIR/bin/activate


# Lanzar la aplicación
echo "Iniciando servidor en local..."
cd backend
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# Desactivar el entorno virtual al terminar
deactivate
