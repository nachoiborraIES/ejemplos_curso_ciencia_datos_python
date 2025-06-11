# Programa que realiza una serie de cálculos estadísticos sobre un dataset
# de jugadores de baloncesto

import pandas as pd
from scipy.stats import skew

datos = pd.read_csv('players.csv')

# Eliminar filas con nulos y contar cuántas son
filas_iniciales = len(datos)
datos.dropna(inplace=True)
filas_finales = len(datos)
print("Eliminadas", filas_iniciales - filas_finales, "filas de", filas_iniciales)

# Convertir altura a cm
datos['height_cm'] = datos['height_feet'] * 30.48

# Convertir peso a Kg
datos['weight_kg'] = datos['weight_pounds'] * 0.45

# Selección de columnas
datos = datos[['first_name', 'last_name', 'position', 'team', 'height_cm', 'weight_kg']]
print(datos.head())

# Jugador más alto
jugador_mas_alto = datos.loc[datos['height_cm'].idxmax()]
print("Jugador más alto:", jugador_mas_alto['first_name'], 
    jugador_mas_alto['last_name'], jugador_mas_alto['height_cm'], "cm")

# Jugador con menos peso
jugador_menos_peso = datos.loc[datos['weight_kg'].idxmin()]
print("Jugador menos peso:", jugador_menos_peso['first_name'], 
    jugador_menos_peso['last_name'], jugador_menos_peso['weight_kg'], "kg")

# Asimetría de alturas
media_alturas = datos['height_cm'].mean()
mediana_alturas = datos['height_cm'].median()
asimetria_alturas = skew(datos['height_cm'])
print("Media alturas:", media_alturas)
print("Mediana alturas:", mediana_alturas)
print("Asimetría alturas:", asimetria_alturas)