"""Configuración del proyecto: carga credenciales y parámetros desde el `.env`.

Cada motor usa su propio prefijo (activo: `MSSQL_`); nunca un genérico `DB_`.
Para usar otro motor, descomenta su grupo aquí y en el `.env`.
"""

import os

from dotenv import load_dotenv

load_dotenv()

# === SQL Server (activo) ===
MSSQL_HOST = os.getenv("MSSQL_HOST")
MSSQL_USER = os.getenv("MSSQL_USER")
MSSQL_PASSWORD = os.getenv("MSSQL_PASSWORD")
MSSQL_DRIVER = "ODBC Driver 17 for SQL Server"
# Opcionales: None si no se definen -> URL.create() los omite (caso DataWarehouse).
MSSQL_NAME = os.getenv("MSSQL_NAME") or None
_mssql_port = os.getenv("MSSQL_PORT")
MSSQL_PORT = int(_mssql_port) if _mssql_port else None

# === (OPCIONAL) PostgreSQL — descomentar si se usa ===
# PG_HOST = os.getenv("PG_HOST")
# PG_USER = os.getenv("PG_USER")
# PG_PASSWORD = os.getenv("PG_PASSWORD")
# PG_NAME = os.getenv("PG_NAME") or None
# _pg_port = os.getenv("PG_PORT")
# PG_PORT = int(_pg_port) if _pg_port else None

# === (OPCIONAL) Oracle — descomentar si se usa ===
# ORACLE_HOST = os.getenv("ORACLE_HOST")
# ORACLE_USER = os.getenv("ORACLE_USER")
# ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD")
# ORACLE_NAME = os.getenv("ORACLE_NAME") or None
# _oracle_port = os.getenv("ORACLE_PORT")
# ORACLE_PORT = int(_oracle_port) if _oracle_port else None

# === (OPCIONAL) Túnel SSH — ver README_HELIX §11 Caso B; por defecto, conexión directa ===
# SSH_HOST = os.getenv("SSH_HOST")
# SSH_USER = os.getenv("SSH_USER")
# SSH_PASSWORD = os.getenv("SSH_PASSWORD")
# _ssh_port = os.getenv("SSH_PORT")
# SSH_PORT = int(_ssh_port) if _ssh_port else None
