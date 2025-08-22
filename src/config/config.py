"""
Módulo de configuración para el proyecto ReqPoblaciónAPS.
Maneja parámetros, credenciales y configuraciones del lago de datos.
"""

from dotenv import load_dotenv
import os

load_dotenv()

DB_SERVER = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DRIVER = "ODBC Driver 17 for SQL Server"
DB_NAME = os.getenv("DB_NAME")