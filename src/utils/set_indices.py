"""
Módulo para establecer índices de observaciones.
Define claves primarias y índices para el análisis.
"""

"""
Establece índices y elimina duplicados.
"""


def set_unique_index(df, index_col):
    df = df.drop_duplicates(subset=[index_col], keep="first")
    df = df.set_index(index_col, verify_integrity=False)
    return df
