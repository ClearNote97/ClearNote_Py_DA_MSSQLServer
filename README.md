# 🐍 Plantilla Dev Container para Ciencia de Datos en Python con MS SQL Server — ClearNote Py DA

Bienvenido a la plantilla oficial **ClearNote Py DA**, un entorno ligero, reproducible y altamente portable para desarrollo de análisis de datos con Python y MS SQL Server dentro de contenedores usando Visual Studio Code + Docker.

---

## 📁 Estructura del Proyecto

```
.
├── data/                    # Directorio para datos
│   ├── other/              # Datos de entrada sin procesar en formatos distintos a SQL
│   ├── sql/              # Consultas y utilidades SQL
├── notebooks/              # Jupyter notebooks
│   └── Notebook.py        # Notebook principal en formato .py
├── output/             # Datos procesados y resultados
├── scripts/               
│   └── run_pipeline.py    # Script para ejecutar el pipeline completo
├── src/                    # Código fuente del proyecto
│   ├── config/            # Configuraciones
│   ├── pipelines/         # Pipelines de datos
│   └── utils/            # Funciones auxiliares
└── requirements.txt       # Dependencias del proyecto (Estándar)
```

## 🎯 Propósito

Esta plantilla está diseñada para:

- Ejecutar proyectos de ciencia de datos **sin instalar nada en tu sistema anfitrión**
- Trabajar con MS SQL Server y Python de forma integrada
- Usar `.py` y `.ipynb` de forma interactiva con **Jupyter Interactive Window**
- Mantener una estructura organizada para proyectos de análisis de datos
- Integrar herramientas modernas de desarrollo: formateadores, linters y depuradores
- Trabajar en carpetas sincronizadas (como OneDrive) sin conflictos de permisos

---

## 🧱 Estructura del contenedor

- **Imagen base**: `python:3.13.2-slim-bookworm`
- **Kernel interactivo**: `ipykernel` incluido
- **Gestor de paquetes**: `pip`, configurado para instalar automáticamente desde `requirements.txt`
- **Usuario por defecto**: `root`, para evitar errores de permisos en carpetas compartidas
- **Extensiones VS Code**: preconfiguradas para Python, Jupyter, SQL Tools, Copilot, Black, etc.
- **Utilidades de datos**: Pandas, NumPy y otras librerías esenciales
- **Conexión a SQL Server**: Configuración preestablecida para pyodbc y SQL Tools

---

## ⚙️ Instrucciones de uso
### 1. Clona este repositorio y renombrar la carpeta
```bash
cd tu_ruta/

git clone https://github.com/ClearNote97/ClearNote_Py_DA_MSSQLServer.git

cd ClearNote_Py_DA_MSSQLServer

```
### 2. Desvincula el repositorio original (opcional)
Este paso elimina la conexión con el repositorio de origen en GitHub, para que puedas comenzar un proyecto independiente desde cero:

```bash
rm -rf .git
```

Se le cambia el nombre a la carpeta, para que se diferencie de la plantilla original:

```bash
cd ~

cd tu_ruta/

mv ClearNote_Py_DA_MSSQLServer nuevo_nombre

cd nuevo_nombre
```

Se inicia un nuevo proyecto con GIT:

```bash
git init
git add .
git commit -m "Proyecto inicial basado en plantilla ClearNote Py DA con Conexión a MS SQL Server"
```

- 💡 Luego puedes conectar tu propio repositorio con:

```bash
git remote add origin https://github.com/tu_usuario/tu_repositorio.git
git push -u origin main
```

### 3. Abre la carpeta en Visual Studio Code

Selecciona Reopen in Container cuando se detecte automáticamente el Dev Container.

### 4. Instala dependencias

Después de crear el contenedor, se ejecutará automáticamente:

```bash
pip install -r requirements.txt
```

Puedes personalizar este archivo para incluir tus propias librerías.

---

## 🧪 ¿Qué puedes hacer aquí?
| Tarea                           | Disponible ✅                      |
| ------------------------------- | --------------------------------- |
| Ejecutar scripts `.py`          | ✅                                 |
| Usar `shift + enter` en código  | ✅ (modo interactivo sin notebook) |
| Ejecutar notebooks `.ipynb`     | ✅                                 |
| Consultas SQL interactivas      | ✅                                 |
| Pipelines de datos automatizados| ✅                                 |
| Formato automático con Black    | ✅                                 |
| Depurar scripts con breakpoints | ✅                                 |
| Correr análisis reproducibles   | ✅                                 |
| Usar Git y control de versiones | ✅                                 |

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

---

## 🔍 Recomendaciones adicionales

### Configuración del Entorno
- Para interacción con .py en modo notebook, asegúrate de instalar ipykernel (ya lo incluye esta imagen)
- Configura las credenciales de SQL Server en `src/config/config.py`
- Utiliza las funciones predefinidas en `src/utils/` para operaciones comunes

### Ejecución del Pipeline
1. Coloca tus datos de entrada en `data/input/`
2. Ajusta las consultas SQL en `data/sql/main_query.sql`
3. Configura los parámetros en `src/config/config.py`
4. Ejecuta el pipeline completo con `python scripts/run_pipeline.py`

### VS Code Settings
```json
"jupyter.interactiveWindow.textEditor.executeSelection": true,
"remote.containers.mountWaylandSocket": false
```

### Buenas Prácticas
- Mantén las consultas SQL en archivos `.sql` separados
- Documenta las transformaciones de datos en los notebooks
- Utiliza el control de versiones para los cambios en el código
- Mantén los datos sensibles fuera del repositorio

---

## ⚖️ Licencia
Distribuido bajo la licencia [MIT](https://opensource.org/license/MIT). Puedes copiar, modificar y reutilizar libremente esta plantilla.

---

**MSc. Nicolás Enrique Valencia Santiago**

# README Modificable:
Vale la pena aclarar que el contenido de este README.md debe de ser modificado para adaptarse al proyecto para el que se quiera usar.