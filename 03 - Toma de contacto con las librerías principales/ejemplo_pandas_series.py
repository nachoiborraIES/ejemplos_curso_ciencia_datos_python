# Ejemplo de uso de series en Pandas

import pandas as pd

# Creación a partir de listas
datos = [1, 5, 10]
serie = pd.Series(datos)
print(datos[0])

# Reindexación
serie = pd.Series(datos, index=['a', 'b', 'c'])
print(serie['b'])
print(serie.iloc[1])

# Creación a partir de diccionarios
datos = {'a':1, 'b':5, 'c':10}
serie = pd.Series(datos)
print(datos['c'])