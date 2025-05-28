# Ejemplo de creación de arrays con NumPy

import numpy as np

# Formas de crear arrays

# Indicando sus elementos en lista/tupla
vector = np.array([1, 2, 3, 4, 5])
vector2 = np.array((2, 4, 6, 8))
vector3 = np.array([1, 2, 3], dtype = np.float32)
print("vector:", vector)
print("vector2:", vector2)
print("vector3:", vector3)
tabla = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("tabla:", tabla)

# Rellenando con unos o ceros
ceros = np.zeros(2)
unos = np.ones(3)
unosEnteros = np.ones(3).astype(np.int32)
unos2 = np.ones((2, 3))
print("ceros:", ceros)
print("unos:", unos)
print("unosEnteros:", unosEnteros)
print("unos2:", unos2)

# Rellenando con otros datos
cuatros = np.full(6, 4)
tabla1 = np.full((3, 2), 4)
tabla2 = np.full((3, 2), [3, 4])
print("cuatros:", cuatros)
print("tabla1:", tabla1)
print("tabla2:", tabla2)

# Definiendo una secuencia de valores
secuencia1 = np.arange(4)
secuencia2 = np.arange(1, 5)
secuencia3 = np.arange(0, 10, 2)
print("secuencia1:", secuencia1)
print("secuencia2:", secuencia2)
print("secuencia3:", secuencia3)
secuencia = np.linspace(0, 20, 5)
print("secuencia:", secuencia)

# Acceso a casillas
print("casilla 0 de vector:", vector[0])
print("casilla [1, 2] de tabla:", tabla[1, 2])

# Fancy indexing
print("selección de elementos 1 y 3:", vector[[1, 3]])

# Otras propiedades
print("Dimensiones de vector:", vector.ndim)
print("Filas de tabla:", tabla.shape[0])
print("Columnas de tabla:", tabla.shape[1])
print("Casillas de tabla:", tabla.size)
print("Tipo de tabla:", tabla.dtype)
