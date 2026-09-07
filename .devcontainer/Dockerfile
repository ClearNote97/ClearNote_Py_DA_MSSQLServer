# Dev Container para análisis de datos en Python CON conexión a SQL.
# Ejemplo activo: SQL Server (pyodbc + ODBC Driver 17). PostgreSQL y Oracle: ver bloques comentados.

# ✅ Imagen base ligera de Python 3.14.5 sobre Debian ("bookworm" = Debian 12)
FROM python:3.14.5-slim-bookworm

# ⚙️ Evita mensajes interactivos durante instalaciones con apt
ENV DEBIAN_FRONTEND=noninteractive

# 🔧 Dependencias de sistema base + SQL Server (msodbcsql17).
# msodbcsql17 requiere unixodbc-dev. La clave del repo de Microsoft se instala con el método
# moderno de keyring: apt-key está DEPRECADO y removido en Debian 12 (bookworm).
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        curl \
        gnupg \
    && install -d -m 0755 /etc/apt/keyrings \
    && curl -fsSL https://packages.microsoft.com/keys/microsoft.asc \
        | gpg --dearmor -o /etc/apt/keyrings/microsoft.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/microsoft.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" \
        > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y --no-install-recommends \
        unixodbc-dev \
        msodbcsql17 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 🐘 (OPCIONAL) PostgreSQL — descomentar si te conectas a Postgres.
#   - Driver Python: "psycopg[binary]" (no necesita system deps).
#   - Solo si compilas psycopg desde fuente: libpq-dev.
# RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev \
#     && apt-get clean && rm -rf /var/lib/apt/lists/*

# 🅾️ (OPCIONAL) Oracle — descomentar si te conectas a Oracle.
#   - Driver Python: "oracledb". En modo "thin" (por defecto) NO necesita nada del sistema.
#   - Solo el modo "thick" requiere Oracle Instant Client (libaio1 + descarga del client).
# RUN apt-get update && apt-get install -y --no-install-recommends libaio1 \
#     && apt-get clean && rm -rf /var/lib/apt/lists/*

# 🔒 (OPCIONAL) Conexión por TÚNEL SSH — ver README_HELIX §11 Caso B (por defecto usamos conexión directa).
#   sshtunnel arrastra cryptography, que puede requerir compilar:
# RUN apt-get update && apt-get install -y --no-install-recommends libffi-dev libssl-dev \
#     && apt-get clean && rm -rf /var/lib/apt/lists/*
#     # Si cryptography compila desde fuente, agrega también: rustc cargo

# 📦 Instalar uv desde la imagen oficial de Astral (versión fijada)
COPY --from=ghcr.io/astral-sh/uv:0.11.13 /uv /uvx /bin/
