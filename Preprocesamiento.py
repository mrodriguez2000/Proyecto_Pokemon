import json

def renombrar_columnas(df, path_json):
    with open(path_json, "r", encoding="utf-8") as file:
        columnas = json.load(file)
    df = df.rename(columns=columnas)
    return df

def eliminar_total(df):
    df = df.drop("total_base_stats", axis=1, errors="ignore")
    df["estadistica_base_total"] = df[["hp", "ataque", "defensa", "ataque_especial", "defensa_especial", "velocidad"]].sum(axis=1)
    return df

def traducir_columnas(df):
    df["categoria"] = df["categoria"].replace({
        "legendary": "legendario",
        "mythical": "mitico",
        "ultra beast": "ultra entes",
        "paradox": "paradoja"
    })
    return df

def traducir_tipos(df):
    df[["primer_tipo", "segundo_tipo"]] = df[["primer_tipo", "segundo_tipo"]].replace({
        'grass': "planta", 'fire': "fuego", 'water': "agua", 'bug': "bicho", 'normal': "normal",
        'poison': "veneno", 'electric': "electrico", 'ground': "tierra", 'fairy': "hada",
        'fighting': "lucha", 'psychic': "psiquico", 'rock': "roca", 'ghost': "fantasma",
        'ice': "hielo", 'dark': "siniestro", 'steel': "acero", 'flying': "volador"
    })
    return df