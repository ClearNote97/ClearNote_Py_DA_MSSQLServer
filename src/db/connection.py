"""Fábrica de engines SQLAlchemy por motor de base de datos.

Ejemplo **activo**: SQL Server (pyodbc). PostgreSQL y Oracle quedan como referencia comentada.
El código de conexión es *código*, por eso vive en `src/`; las consultas `.sql` viven en `data/sql/`.
Un engine por motor, con nombre propio (nunca un `get_engine()` genérico).
"""

from sqlalchemy import create_engine
from sqlalchemy.engine import URL, Engine

from src.config import config


def get_engine_mssql() -> Engine:
    """Crea el engine de SQL Server (pyodbc) usando `URL.create()`.

    `URL.create()` escapa solo usuario/contraseña/parámetros — sin `quote_plus` manual
    ni `odbc_connect`. `MSSQL_NAME` y `MSSQL_PORT` son **opcionales**: si vienen `None`,
    se omiten (útil al trabajar contra un DataWarehouse sin una única base de datos).
    """
    url = URL.create(
        "mssql+pyodbc",
        username=config.MSSQL_USER,
        password=config.MSSQL_PASSWORD,
        host=config.MSSQL_HOST,
        port=config.MSSQL_PORT,
        database=config.MSSQL_NAME,
        query={"driver": config.MSSQL_DRIVER},
    )
    return create_engine(url)


# ---------------------------------------------------------------------------
# OTROS MOTORES (referencia). Para usar uno: descomenta su función, instala el
# driver (requirements.txt), agrega su grupo de variables en config.py + .env,
# y —si aplica— sus system deps en .devcontainer/Dockerfile.
# ---------------------------------------------------------------------------

# PostgreSQL — dialecto "postgresql+psycopg"; paquete: "psycopg[binary]" (uv add / requirements.txt)
# def get_engine_postgres() -> Engine:
#     url = URL.create(
#         "postgresql+psycopg",
#         username=config.PG_USER,
#         password=config.PG_PASSWORD,
#         host=config.PG_HOST,
#         port=config.PG_PORT,       # opcional
#         database=config.PG_NAME,   # opcional
#     )
#     return create_engine(url)
#
# PostgreSQL por TÚNEL SSH (conexión indirecta): ver README_HELIX §11 Caso B.
# Se abre el túnel antes de crear el engine y se devuelve (engine, tunnel);
# hay que llamar tunnel.stop() al terminar. Se mantiene comentado a propósito:
# por defecto usamos conexión DIRECTA.

# Oracle — dialecto "oracle+oracledb"; paquete: "oracledb" (uv add / requirements.txt); modo "thin" no requiere Instant Client
# def get_engine_oracle() -> Engine:
#     url = URL.create(
#         "oracle+oracledb",
#         username=config.ORACLE_USER,
#         password=config.ORACLE_PASSWORD,
#         host=config.ORACLE_HOST,
#         port=config.ORACLE_PORT,
#         database=config.ORACLE_NAME,   # service_name / SID según tu caso
#     )
#     return create_engine(url)
