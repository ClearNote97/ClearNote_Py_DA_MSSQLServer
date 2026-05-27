# 🐍 Plantilla Dev Container para Ciencia de Datos en Python con MS SQL Server — ClearNote Py DA

Bienvenido a la plantilla oficial **ClearNote Py DA**, un entorno ligero, reproducible y altamente portable para desarrollo de análisis de datos con Python y MS SQL Server dentro de contenedores usando **Visual Studio Code + Dev Containers + Docker + uv**.

## 📁 Estructura del Proyecto

```
.
├── data/                    # Directorio para datos
│   ├── other/              # Datos de entrada sin procesar en formatos distintos a SQL
│   ├── sql/                # Consultas y utilidades SQL
├── notebooks/              # Jupyter notebooks
│   └── Notebook.py        # Notebook principal en formato .py
├── output/                 # Datos procesados y resultados
├── scripts/               
│   └── run_pipeline.py    # Script para ejecutar el pipeline completo
├── src/                    # Código fuente del proyecto
│   ├── config/            # Configuraciones
│   ├── pipelines/         # Pipelines de datos
│   └── utils/             # Funciones auxiliares
└── requirements.txt        # Dependencias del proyecto (Etapa 1)
```

## 🎯 Propósito

Esta plantilla está diseñada para:

- Ejecutar proyectos de ciencia de datos **sin instalar nada en tu sistema anfitrión**
- Trabajar con MS SQL Server y Python de forma integrada
- Usar `.py` y `.ipynb` de forma interactiva con **Jupyter Interactive Window**
- Mantener una estructura organizada para proyectos de análisis de datos
- Gestionar dependencias con **uv**, un gestor moderno y rápido para proyectos Python
- Facilitar la transición desde un flujo clásico con `requirements.txt` hacia uno más moderno con `pyproject.toml` + `uv.lock`
- Trabajar en carpetas sincronizadas (como OneDrive) sin conflictos de permisos

## 🧱 Estructura del entorno

### Contenedor base

- **Imagen base**: `python:3.14.5-slim-bookworm`
- **Paquetes del sistema**:
  - `build-essential`
  - `ca-certificates`
  - `curl`
  - `gcc`, `g++`
  - `gnupg`
  - `unixodbc-dev`
  - `msodbcsql17`, `mssql-tools`

### Gestión de dependencias

- **Gestor de paquetes/proyectos**: `uv`
- **Versión fijada**: `0.11.13`
- **Instalación de uv**: copiado desde la imagen oficial de Astral
- **Entorno virtual del proyecto**: `.venv/`

### Editor y experiencia de desarrollo

- **Editor principal**: Visual Studio Code
- **Extensiones preconfiguradas**:
  - Python
  - Pylance
  - Ruff
  - Jupyter
  - Better TOML
  - GitHub Copilot
  - Path Intellisense
  - Material Icon Theme

### Intérprete configurado

La plantilla apunta automáticamente al intérprete dentro del entorno virtual:

```bash
${workspaceFolder}/.venv/bin/python
```

## ⚙️ Flujo de inicialización del proyecto

Cuando el contenedor se crea por primera vez, el `postCreateCommand` detecta automáticamente el tipo de proyecto y actúa en consecuencia:

### Caso 1: ya existe `pyproject.toml`

- Si también existe `uv.lock`:
  - ejecuta `uv sync --locked`
- Si no existe `uv.lock`:
  - ejecuta `uv lock && uv sync`

### Caso 2: todavía existe solo `requirements.txt`

- ejecuta `uv init --no-package --no-workspace .`
- elimina el archivo `main.py` generado por defecto
- importa dependencias desde `requirements.txt` con:
  - `uv add -r requirements.txt`

### Caso 3: no existe ninguno

- el proceso falla y muestra un mensaje indicando que falta `pyproject.toml` o `requirements.txt`

## 📂 Filosofía de esta plantilla

Esta plantilla adopta un enfoque de transición en dos etapas:

### Etapa 1: compatibilidad con `requirements.txt`

Ideal para proyectos existentes que todavía no migran por completo a `pyproject.toml`.

Permite:

- seguir usando la estructura tradicional
- empezar a trabajar con `uv`
- crear la base para migrar a lockfiles reproducibles

### Etapa 2: migración total a `pyproject.toml` + `uv.lock`

Recomendada para nuevos proyectos o para consolidar entornos reproducibles.

Ventajas:

- mejor manejo de dependencias
- lockfile reproducible
- flujo más moderno y mantenible
- integración más natural con tooling actual de Python

## 🚀 Instrucciones de uso

### 1. Clona este repositorio

```bash
cd tu_ruta/
git clone https://github.com/ClearNote97/ClearNote_Py_DA_MSSQLServer.git
cd ClearNote_Py_DA_MSSQLServer
```

### 2. Desvincula el repositorio original (opcional)

Si quieres usar esta plantilla como base para un proyecto nuevo:

```bash
rm -rf .git
```

Luego renombra la carpeta:

```bash
cd ..
mv ClearNote_Py_DA_MSSQLServer nuevo_nombre
cd nuevo_nombre
```

Inicializa tu nuevo repositorio:

```bash
git init
git add .
git commit -m "Proyecto inicial basado en plantilla ClearNote Py DA con Conexión a MS SQL Server"
```

Y conecta tu propio repositorio si lo deseas:

```bash
git remote add origin https://github.com/tu_usuario/tu_repositorio.git
git push -u origin main
```

### 3. Abre la carpeta en Visual Studio Code

Cuando VS Code detecte la configuración, selecciona:

**Reopen in Container**

### 4. Espera la inicialización automática

Durante la creación del contenedor, la plantilla:

- instala `uv`
- detecta si trabajas con `pyproject.toml` o `requirements.txt`
- prepara el entorno virtual `.venv`
- instala o sincroniza dependencias

No necesitas correr `pip install` manualmente.

## 🧪 ¿Qué puedes hacer aquí?

| Tarea | Disponible ✅ |
|---|---|
| Ejecutar scripts `.py` | ✅ |
| Usar notebooks `.ipynb` | ✅ |
| Ejecutar código por bloques | ✅ |
| Consultas SQL interactivas | ✅ |
| Conexión a MS SQL Server | ✅ |
| Pipelines de datos automatizados | ✅ |
| Formatear código automáticamente con Ruff | ✅ |
| Organizar imports | ✅ |
| Hacer análisis reproducibles | ✅ |
| Depurar scripts con breakpoints | ✅ |
| Gestionar dependencias con `uv` | ✅ |
| Trabajar dentro de contenedor aislado | ✅ |
| Usar Git y control de versiones | ✅ |

## 📊 Componentes Principales

### Pipeline de Datos (`src/pipelines/`)
- `main_pipeline.py`: Orquesta el flujo completo de procesamiento de datos

### Utilidades SQL (`data/sql/`)
- `main_query.sql`: Consultas SQL principales
- `sql_utils.py`: Funciones auxiliares para interactuar con SQL Server

### Utilidades de Datos (`src/utils/`)
- Módulos para limpieza, transformación y exportación de datos
- Funciones reutilizables para manipulación de datasets
- Herramientas para estandarización y formateo de variables

## 📦 Sobre `uv` en esta plantilla

`uv` reemplaza el uso tradicional de `pip` como comando principal del flujo de trabajo.

### ¿Qué aporta?

- mayor velocidad
- manejo moderno de dependencias
- lockfiles reproducibles
- integración con proyectos Python actuales
- mejor experiencia dentro de contenedores reproducibles

### Importante

Aunque la imagen base de Python pueda traer `pip` instalado internamente, esta plantilla **no lo usa como herramienta de trabajo**. Toda la gestión del entorno y dependencias se realiza con `uv`.

## 🧹 Archivos importantes del proyecto

### Deben versionarse

- `README.md`
- `.devcontainer/devcontainer.json`
- `.devcontainer/Dockerfile`
- `requirements.txt` o `pyproject.toml`
- `uv.lock` cuando exista

### No deben versionarse

- `.venv/`
- `__pycache__/`
- `*.pyc`
- `.env`

Un `.gitignore` mínimo recomendado sería:

```gitignore
.env
__pycache__/
*.pyc
.venv/
```

## 🔍 Recomendaciones

### Configuración del Entorno
- Configura las credenciales de SQL Server en `.env`
- Utiliza las funciones predefinidas en `src/utils/` para operaciones comunes
- Si usas notebooks o ejecución interactiva, valida que `ipykernel` esté incluido en tus dependencias

### Ejecución del Pipeline
1. Coloca tus datos de entrada en `data/other/` o `data/sql/`
2. Ajusta las consultas SQL en `data/sql/main_query.sql`
3. Configura los parámetros en `src/config/config.py`
4. Ejecuta el pipeline completo con `python scripts/run_pipeline.py`

### Buenas Prácticas
- Mantén las consultas SQL en archivos `.sql` separados
- Documenta las transformaciones de datos en los notebooks
- Utiliza el control de versiones para los cambios en el código
- Mantén los datos sensibles fuera del repositorio
- Si ya migraste a `uv.lock`, consérvalo en el repositorio

## ⚖️ Licencia

Distribuido bajo la licencia [MIT](https://opensource.org/license/MIT). Puedes copiar, modificar y reutilizar libremente esta plantilla.

## ✍️ Autor

**MSc. Nicolás Enrique Valencia Santiago**

## 📝 Nota final

Este `README.md` está pensado como base y debe adaptarse según el tipo de proyecto que se construya a partir de esta plantilla.
