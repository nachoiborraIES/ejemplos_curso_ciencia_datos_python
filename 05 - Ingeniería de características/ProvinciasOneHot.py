# Programa que aplica codificación "one hot" a la columna "provincia" del
# dataset

import pandas as pd

datos = pd.read_csv('parques_eolicos.csv', sep=';')

# Codificamos con "one hot" el campo "provincia"

datos = pd.get_dummies(datos, columns=['provincia'], prefix='prov')
print(datos.head())