"""
Funciones para conexión y consulta a la base de datos.
"""

import sqlalchemy
import urllib
from src.config import config


def get_engine():
    connection_str = (
        f"DRIVER={{{config.DB_DRIVER}}};"
        f"SERVER={config.DB_SERVER};"
        f"UID={config.DB_USER};"
        f"PWD={config.DB_PASSWORD};"
    )
    connection_str_quoted = urllib.parse.quote_plus(connection_str)
    connection_uri = f"mssql+pyodbc:///?odbc_connect={connection_str_quoted}"
    return sqlalchemy.create_engine(connection_uri)


def run_query(query, engine):
    return engine.execute(query)