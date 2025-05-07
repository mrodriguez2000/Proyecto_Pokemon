import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from archivo_principal import cargar_datos

# Cargar y procesar los datos
df = cargar_datos(
    "G:\\Mi unidad\\Carrera de Python\\Curso basico\\Matplotlib\\pokemon_dataset.csv",
    "G:\\Mi unidad\\Carrera de Python\\Curso basico\\Matplotlib\\columnas.json"
)

# Agrupando cantidad de Pokemon por tipo

def tipo_pokemon():
    pokemon_type = df.groupby("primer_tipo").agg(cantidad_pokemons = ("pokemon_id", "count")).sort_values(by = "cantidad_pokemons", ascending = False).reset_index()

    return pokemon_type

# Estadistica promedio de Pokemon por tipo
def estadistica_promedio_pokemon():
    pokemon_category_stats = df.groupby("categoria").agg(estadistica_promedio=("estadistica_base_total", "mean")).sort_values(by="estadistica_promedio", ascending=False).reset_index().round(2)

    return pokemon_category_stats

# Consultar los Pokemon más poderosos
def estadisticas():
    pokemon_name_stats = df.groupby(["categoria", "nombre_pokemon"]).agg(estadistica_total=("estadistica_base_total", "sum")).reset_index().sort_values(by="estadistica_total", ascending=False)

    return pokemon_name_stats


if __name__ == "__main__":
    print(tipo_pokemon())
    print(estadistica_promedio_pokemon())
    print(estadisticas())