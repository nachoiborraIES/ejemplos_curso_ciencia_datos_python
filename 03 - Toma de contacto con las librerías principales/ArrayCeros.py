# Programa que define un array de 10 ceros enteros, 
# cambia un valor y lo muestra usando NumPy

import numpy as np

ceros = np.zeros(10).astype(np.int32)
ceros[2] = 1
print(ceros)
