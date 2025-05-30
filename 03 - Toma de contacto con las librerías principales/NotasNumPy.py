# Programa que gestiona un conjunto de notas a través de NumPy

import numpy as np

secuencia = input("Introduce las notas separadas por espacios:\n")
notas = list(map(int, secuencia.split(' ')))

# Crear array unidimensional de notas
datos = np.array(notas)
print("Datos iniciales:", datos)

# Ordenar notas de mayor a menor
datosOrdenados = -np.sort(-datos)
print("Datos ordenados:", datosOrdenados)

# Notas aprobadas
datosAprobados = datosOrdenados[datosOrdenados >= 5]
print("Datos aprobados:", datosAprobados)

# Media de notas aprobadas
print(f'Media de notas aprobadas: {datosAprobados.mean()}')
