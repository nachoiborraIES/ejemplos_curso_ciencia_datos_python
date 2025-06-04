# Ejemplo de operaciones avanzadas con Pandas

import numpy as np
import pandas as pd

datos = { 'Nombre': ['Nacho', 'Juan', 'Ana'],
    'Email': ['nacho@gmail.com', 'jperez@gmail.com', 'anaib@gmail.com'],
    'Edad': [44, 70, 40],
    'Telefono': ['611223344', '699887766', '619283746'] }
df = pd.DataFrame(datos)

# Añadir filas y columnas

df.loc[len(df)] = ['Sergio', 'sergio@gmail.com', 15, '600112233']
df['Localidad'] = ['Alicante', 'Valencia', 'Castellón', 'Alicante']
print(df)

# Borrar filas y columnas
# df.drop(3, axis = 0, inplace=True)
# df.drop('Localidad', axis = 1, inplace=True)
# print(df)

# Filtrados

seleccion_edad = df[(df['Edad'] >= 30) & (df['Edad'] <= 50)]
print("Selección de edades:")
print(seleccion_edad)

localidades = ['Alicante', 'Valencia']
seleccion_localidad = df[~df['Localidad'].isin(localidades)]
print("Selección de localidades:")
print(seleccion_localidad)

# Reemplazos

df['Cod_Localidad'] = df['Localidad'].map({'Alicante': 'A', 'Valencia': 'V',
    'Castellón': 'C'})
df['Localidad'] = df['Localidad'].str.upper()
print(df)

# Ordenaciones

df = df.sort_values(by='Edad', ascending=False)
df.reset_index(drop=True, inplace=True)
print(df)

# Concatenación

datos2 = { 'Nombre': ['Mario', 'Laura'],
    'Email': ['mario@gmail.com', 'laura@hotmail.com'],
    'Edad': [34, 32],
    'Telefono': ['612984538', '600918273'],
    'Localidad': ['ALICANTE', 'CASTELLÓN'],
    'Cod_Localidad': ['A', 'C'] }
df2 = pd.DataFrame(datos2)

df = pd.concat([df, df2], axis=0)
df.reset_index(drop=True, inplace=True)
print(df)

# Agrupaciones

df_grupos = df[['Localidad', 'Edad']]
print("Media de edades por localidad:")
print(df_grupos.groupby('Localidad').mean())

# Trabajo con fechas

df['Fecha'] = ['24/10/2015', '20/09/2011', '27/04/2018', '07/03/2013',
    '05/04/2018', '15/08/2018']
print(df)
print(df.dtypes)
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')
print(df.dtypes)
df = df.set_index('Fecha').sort_index()
print(df.loc['2018-04'])

# Otros cálculos

print("Cuántas localidades hay de cada tipo:")
print(df['Localidad'].value_counts())

print("Categoría por edad")
df['Categoria_Edad'] = pd.cut(df['Edad'],
    bins = [0, 12, 18, 65, np.inf],
    labels = ['Niño', 'Adolescente', 'Adulto', 'Anciano'])
print(df)

print("Localidades distintas:", df['Localidad'].unique())

print("Media de edad:", df['Edad'].mean())