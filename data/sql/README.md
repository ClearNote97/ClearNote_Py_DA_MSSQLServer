# `data/sql/` — catálogo de consultas

Aquí viven **solo archivos `.sql`** (el SQL es *dato*, no código Python). Una consulta por archivo,
con nombre autodescriptivo (`snake_case`, acción + objeto), para que listar la carpeta revele el
repertorio sin abrir nada.

- El **código de conexión** (la fábrica de engine) NO vive aquí: está en `src/db/connection.py`.
- Las consultas se leen desde Python y se ejecutan con `pd.read_sql`. Ver `README_HELIX.md` §11.
