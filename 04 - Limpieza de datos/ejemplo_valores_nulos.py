# Ejemplos de limpieza de valores nulos

import numpy as np
import pandas as pd

datosIniciales = {'Nombre': ['Juan', 'Ana', 'Mario', 'Laura'],
    'Edad': [70, np.nan, 30, 26],
    'Peso': [75, 70, np.nan, 70]}
datos = pd.DataFrame(datosIniciales)

# Detección/Conteo de valores nulos

print("Número de casillas nulas:")
conteo_nulos = datos.isnull().sum()
print(conteo_nulos)
print(conteo_nulos['Edad'])

valores_nulos = datos.isnull().sum().sort_values(ascending=False)
ratio_nulos = (valores_nulos / len(datos)).reset_index()
ratio_nulos.columns = ['Característica', 'RatioNulos']
print("Tabla con ratios de nulos ordenada:")
print(ratio_nulos)

# Reemplazo/Imputación de valores

datos['Edad'] = datos['Edad'].fillna(datos['Edad'].mean())
datos['Peso'] = datos['Peso'].fillna(datos['Peso'].mode()[0])

print("Tabla con valores reemplazados:")
print(datos)