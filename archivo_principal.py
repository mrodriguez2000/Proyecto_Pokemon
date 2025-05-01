import pandas as pd
from Utilidades import (
    renombrar_columnas,
    eliminar_total,
    traducir_columnas,
    traducir_tipos
)

def cargar_datos(ruta_csv, ruta_json):
    # Cargar datos
    df = pd.read_csv(ruta_csv)
    
    # Procesamiento paso a paso
    df = renombrar_columnas(df, ruta_json)
    df = eliminar_total(df)
    df = traducir_columnas(df)
    df = traducir_tipos(df)

    return df

if __name__ == "__main__":
    ruta_csv = "G:\\Mi unidad\\Carrera de Python\\Curso basico\\Matplotlib\\pokemon_dataset.csv"
    ruta_json = "G:\\Mi unidad\\Carrera de Python\\Curso basico\\Matplotlib\\columnas.json"

    df = cargar_datos(ruta_csv, ruta_json)