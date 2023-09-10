import difflib

# Lista de nombres conocidos y sus IATA code en minúsculas
nombres_abreviados = {
    "ciudad de méxico": ["ciudad de méxico", "mex", "cdmx"],
    "guadalajara": ["guadalajara", "gdl"],
    "cancun": ["cancun", "cun"],
    "tijuana": ["tijuana", "tij"],
    "puerto vallarta": ["puerto vallarta", "pvr"],
    "monterrey": ["monterrey", "mty"]
}

# Función para encontrar el nombre más cercano
def encontrar_nombre_similar(entrada_usuario):
    entrada_usuario = entrada_usuario.lower()  # Convertir a minúsculas
    
    for nombre, abreviaturas in nombres_abreviados.items():
        if entrada_usuario in abreviaturas:
            return nombre
    
    coincidencias = difflib.get_close_matches(entrada_usuario, nombres_abreviados.keys())
    
    if coincidencias:
        return coincidencias[0]
    else:
        return None

