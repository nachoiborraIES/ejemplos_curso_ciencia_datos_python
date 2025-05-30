# Ejemplo de uso de la librería SciPy

from scipy.stats import skew, pearsonr
import numpy as np

# Asimetría
datos = np.array([2, 8, 6, 5, 4, 7, 9, 12, 15, 16, 17, 18])
asimetria = skew(datos)
print("Asimetría:", asimetria)

# Correlación
x = np.array([10, 20, 30, 40, 50])
y = np.array([15, 30, 45, 60, 75])
coef_pearson, p_valor = pearsonr(x, y)
print("Coeficiente de correlación Pearson:", coef_pearson)
print("Valor p:", p_valor)