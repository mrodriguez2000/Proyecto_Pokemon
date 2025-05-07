import plotly.express as px
import plotly.io as pio
from Analisis import (
    tipo_pokemon, estadistica_promedio_pokemon, estadisticas
)
pio.renderers.default = "browser"

try:
    tipo_de_pokemon = tipo_pokemon()
    estadistica_promedio = estadistica_promedio_pokemon()
    estadisticas_de_pokemon = estadisticas()

    # Realizando gráfico de barras
    def grafico_barras(dataset, categoria, variable):
        fig = px.bar(dataset, categoria, variable)
        fig.show()

        return fig
    
    grafico_de_barras = grafico_barras(tipo_de_pokemon, "primer_tipo", "cantidad_pokemons")

    # Realizando gráfico de barras invertidas
    def grafico_pie(dataset, categoria, variable):
        fig2 = px.pie(dataset, categoria, variable)
        fig2.show()

        return fig2
    
    grafico_de_pie = grafico_pie(tipo_de_pokemon, "primer_tipo", "cantidad_pokemons")

except Exception as e:
    print("Ha ocurrido un error: ", e)