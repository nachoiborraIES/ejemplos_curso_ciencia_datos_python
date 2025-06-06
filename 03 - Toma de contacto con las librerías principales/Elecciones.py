# Programa que muestra el resultado de unas elecciones en un gráfico circular

import numpy as np
import matplotlib.pyplot as plt

partidos = ['PA', 'PB', 'PC', 'PD']
secuencia = input("Escribe los votos separados por espacios (valores de 1 a 4):\n")
votos = list(map(int, secuencia.split(' ')))

# Incrementamos los votos de cada partido
resultado = np.zeros(len(partidos))
for voto in votos:
    if voto >= 1 and voto <= 4:
        resultado[voto-1] += 1

# Actualizamos porcentajes
for i in range(0, len(partidos)):
    porcentaje = resultado[i] * 100 // resultado.sum()
    partidos[i] += " (" + str(porcentaje) + "%)"
    
# Mostramos el gráfico
plt.title("Resultados elecciones")
plt.pie(resultado, labels=partidos)
plt.show()
