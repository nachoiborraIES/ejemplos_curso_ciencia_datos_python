# Programa que carga un archivo CSV e identifica outliers de una columna
# aplicando la técnica de IQR

import numpy as np
import pandas as pd

datos = pd.read_csv('parques_eolicos.csv', sep=';')
outliers = []
Q1, Q3 = np.percentile(datos['potencia'], [25, 75])
IQR = Q3 - Q1

for i in range(0, len(datos)):
    if datos.loc[i,'potencia'] < (Q1 - 0.5*IQR) or \
    datos.loc[i, 'potencia'] > (Q3 + 0.5*IQR):
        outliers.append(datos.loc[i, :])

print(outliers)
print("Total de parques eólicos:", len(datos))
print("Total de outliers:", len(outliers))
