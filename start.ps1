# Script para iniciar la API en Windows

echo "Creando entorno virtual..."
python -m venv venv

echo "Activando entorno virtual..."
.\venv\Scripts\activate

echo "Instalando dependencias desde requirements.txt..."
pip install -r requirements.txt

echo "Iniciando el servidor de FastAPI..."
uvicorn main:app --reload
