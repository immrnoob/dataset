import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Cargar el archivo Excel con respuestas numericas
df = pd.read_excel('respuestas_numerico.xlsx')

# Convertir valores a binarios
umbral = 1
df_binario = df.applymap(lambda x: 1 if x > umbral else 0)

# Aplicar Apriori
frequent_itemsets = apriori(df_binario, min_support=0.1, use_colnames=True)

# Generar reglas de asociación
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Mostrar las reglas de asociación ordenadas por confianza
rules.sort_values(by='confidence', ascending=False, inplace=True)
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# Guardar las reglas de asociación en un nuevo archivo Excel
rules.to_excel('reglas_asociacion.xlsx', index=False)
