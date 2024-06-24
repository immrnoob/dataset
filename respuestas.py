import pandas as pd

# Cargar el archivo Excel original
df = pd.read_excel('respuestas.xlsx')

# Crear un diccionario para mapear las respuestas únicas a números
mapeo_respuestas = {}

# Iterar sobre las columnas (preguntas) del DataFrame
for columna in df.columns:
    # Obtener las respuestas únicas para esta pregunta
    respuestas_unicas = df[columna].unique()
    
    # Asignar un número a cada respuesta única y almacenar en el diccionario
    mapeo_respuestas[columna] = {respuesta: i+1 for i, respuesta in enumerate(respuestas_unicas)}

# Reemplazar las respuestas con los números correspondientes en el DataFrame
df_numerico = df.replace(mapeo_respuestas).infer_objects()

# Guardar el DataFrame con las respuestas numéricas en un nuevo archivo Excel
df_numerico.to_excel('respuestas_numerico.xlsx', index=False)
