# Ejemplo de uso de "one hot encoding"

import pandas as pd

datos = { 'Nacionalidad': ['España', 'Portugal', 'España', 'Francia',
                           'Portugal', 'España'],
          'Edad': [34, 38, 30, 40, 37, 32],
          'Peso': [88.4, 95.6, 90.2, 96.7, 99.3, 82.4],
          'Socio': ['Si', 'Si', 'No', 'No', 'Si', 'Si']}

df = pd.DataFrame(datos)

# One hot con borrado de columna categórica
df2 = pd.get_dummies(df, columns=['Nacionalidad'], prefix='Nac')
print(df2.head())

# One hot sin borrado de columna categorica
columnas_one_hot = pd.get_dummies(df['Nacionalidad'], columns=['Nacionalidad'],
    prefix='Nac')
df = df.join(columnas_one_hot)
print(df.head())