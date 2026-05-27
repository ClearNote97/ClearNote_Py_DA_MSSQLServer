# This Dockerfile is used for the development container in VS Code Remote Containers.
# It sets up a Python environment with the necessary tools for development.

# ✅ Imagen base ligera de Python 3.14.5 sobre Debian (versión "bookworm")
FROM python:3.14.5-slim-bookworm

# ⚙️ Evita mensajes interactivos durante instalaciones con apt
ENV DEBIAN_FRONTEND=noninteractive

# 🔧 Instalación de dependencias del sistema + soporte para SQL Server (msodbcsql17)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    curl \
    gcc \
    g++ \
    gnupg \
    unixodbc-dev \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql17 mssql-tools \
    && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc \
    && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 📦 Instalar uv desde la imagen oficial de Astral (versión fijada)
COPY --from=ghcr.io/astral-sh/uv:0.11.13 /uv /uvx /bin/