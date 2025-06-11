# Programa que aplica un escalado por normalización sobre la potencia de los
# parques eólicos

import pandas as pd

datos = pd.read_csv('parques_eolicos.csv', sep=';')

# Normalizamos la "potencia_unitaria" con valores de 0 a 1

datos['potencia_unitaria_norm'] = (datos['potencia_unitaria'] - \
    datos['potencia_unitaria'].min()) / (datos['potencia_unitaria'].max() - \
    datos['potencia_unitaria'].min())

print(datos.head())