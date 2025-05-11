@echo off
REM Instalar dependencias
pip install -r requirements.txt

REM Crear carpeta data si no existe
if not exist "data" mkdir data

REM Cargar documentos iniciales
python ingest.py

REM Iniciar aplicación
streamlit run main.py