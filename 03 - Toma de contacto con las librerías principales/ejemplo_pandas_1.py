# Ejemplo de uso básico de Pandas

import pandas as pd
from tabulate import tabulate

# Data frames con listas
datos = [['Nacho', 44], ['Juan', 70], ['Ana', 40]]
datosPersonas = pd.DataFrame(datos, columns = ['Nombre', 'Edad'])
print(datosPersonas)

# Data frames con diccionarios
numeros = {'pares': [2, 4, 6, 8], 'impares': [1, 3, 5, 7]}
dataFrame = pd.DataFrame(numeros)
print(dataFrame)

# Data frames a partir de ficheros CSV
df = pd.read_csv('archivo.csv')
print(df.head(2))
print(df.describe())
df.info()
print("Filas:", df.shape[0])
print(tabulate(df, headers='keys', tablefmt='pretty'))