# ✅ Imagen base ligera de Python 3.13.5 sobre Debian (versión "bookworm")
# Usamos la variante "slim" para evitar componentes innecesarios y reducir el tamaño
FROM python:3.13.2-slim-bookworm

# ⚙️ Evita que se muestren mensajes interactivos durante instalaciones con apt
# Esto hace que la imagen se construya automáticamente sin pausas
ENV DEBIAN_FRONTEND=noninteractive

# 🔧 Instalación de dependencias básicas + ipykernel + soporte para SQL Server (msodbcsql17)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    gcc \
    g++ \
    gnupg \
    unixodbc-dev \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir ipykernel \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql17 mssql-tools \
    && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc \
    && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile

# 🧹 Limpieza para reducir el tamaño de la imagen
RUN apt-get clean && rm -rf /var/lib/apt/lists/*