import pandas as pd

# Cargar las reglas de asociación desde el archivo Excel
rules = pd.read_excel('reglas_asociacion.xlsx')

# Desglosar los 'antecedents' y 'consequents' y separarlos en columnas
rules['antecedents'] = rules['antecedents'].apply(lambda x: list(eval(x)))
rules['consequents'] = rules['consequents'].apply(lambda x: list(eval(x)))

# Crear DataFrame separado para los 'antecedents' y 'consequents'
antecedents_df = pd.DataFrame(rules['antecedents'].tolist()).add_prefix('antecedent_')
consequents_df = pd.DataFrame(rules['consequents'].tolist()).add_prefix('consequent_')

# Unir los nuevos DataFrames con el original que contiene 'lift'
result_df = pd.concat([antecedents_df, consequents_df, rules[['lift']]], axis=1)

# Guardar el nuevo DataFrame en un archivo Excel
result_df.to_excel('reglas_asociacion_desglosadas.xlsx', index=False)
