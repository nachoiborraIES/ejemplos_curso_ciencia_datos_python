# Ejemplo de detección y reemplazo de anomalías

import numpy as np
import pandas as pd

valores = np.array([23, 28, 31, 34, 36, 37, 67])
serie = pd.Series(valores)

# Detección basada en la mediana
mediana = np.median(valores)
umbral = 15
outliers = []
for elemento in valores:
    if abs(mediana - elemento) > umbral:
        outliers.append(int(elemento))
print("Anomalías identificadas con la mediana:", outliers)

# Detección basada en la media
media = np.mean(valores)
desviacion = np.std(valores)
outliers = []
for elemento in valores:
    if media - desviacion > elemento or media + desviacion < elemento:
        outliers.append(int(elemento))
print("Anomalías identificadas con la media+desv:", outliers)

# Detección basada en desviación Z

outliers = []
for elemento in valores:
    z = abs(elemento - media) / desviacion
    if z > 1.5:
        outliers.append(int(elemento))
print("Anomalías identificadas con desviación Z:", outliers)

# Detección basada en IQR

Q1, Q3 = np.percentile(valores, [25, 75])
IQR = Q3 - Q1
outliers = []
for elemento in valores:
    if elemento < (Q1 - 1.5 * IQR) or elemento > (Q3 + 1.5 * IQR):
        outliers.append(int(elemento))
print("Anomalías identificadas con rango IQR:", outliers)