# Ejemplo de gestión de filas y columnas

import numpy as np

# Selección de filas y columnas
vector = np.array([1, 2, 3, 4, 5])
tabla = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("tabla[1, :]:", tabla[1, :])
print("tabla[:, 2]:", tabla[:, 2])
print("vector[1:]:", vector[1:])
print("vector[1:3]:", vector[1:3])
print("vector[:4]:", vector[:4])
print("vector[:-1]", vector[:-1])
print("tabla[1:3, 2:]:", tabla[1:3, 2:])

# Concatenaciones
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
print("Concatenación vertical con concatenate:",
    np.concatenate((array1, array2), axis=0))
print("Concatenación horizontal con concatenate:",
    np.concatenate((array1, array2), axis=1))
print("Aplanado dimensional con concatenate:",
    np.concatenate((array1, array2), axis=None))
print("Concatenación vertical con vstack:",
    np.vstack((array1, array2)))

# Redimensionados
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
array2 = np.reshape(array1, (2, 4))
print("array2:", array2)
array3 = np.reshape(array2, (8,))
print("array3:", array3)
tabla_array = array1.reshape(1, -1)
print("tabla_array:", tabla_array)
print(tabla_array.shape)
vector_tabla = tabla.flatten()
print("vector_tabla:", vector_tabla)