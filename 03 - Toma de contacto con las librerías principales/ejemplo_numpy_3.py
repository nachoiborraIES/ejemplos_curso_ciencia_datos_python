# Ejemplos de otras operaciones en NumPy

import numpy as np

# Operaciones estadísticas
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("Media array1:", array1.mean())
print("Mediana array1:", np.median(array1))

# Operaciones escalares
cuadrados = array1 ** 2
print("Cuadrados:", cuadrados)

# Filtrado
pares = array1[array1 % 2 == 0]
print("Pares:", pares)

# Datos aleatorios
np.random.seed(12)
int1 = np.random.randint(100)
print("Número del 0 al 100:", int1)
real1 = np.random.uniform(low = 0.2, high = 0.7, size = 1)
print("Número real de 0.2 a 0.7:", real1)
matriz = np.random.randint(1, 10, size=(3, 5))
print("Matriz 3x5 de enteros del 1 al 10:\n", matriz)
vector = np.random.uniform(low=0.5, high=3.5, size=10)
print("Vector de 10 reales de 0.5 a 3.5:", vector)