# Ejercicio de prueba de la librería SciPy para calcular asimetrías y
# correlaciones de un conjunto de datos
import numpy as np
from scipy.stats import skew, pearsonr, spearmanr

temperaturas = np.array([22, 24, 26, 23, 25, 27, 28, 29, 34, 36])
consumos = np.array([210, 220, 215, 225, 230, 240, 245, 250, 260, 270])

asimetria_temperaturas = skew(temperaturas)
print("Asimetría temperaturas: ", asimetria_temperaturas)

correlacion_pearson, p_pearson = pearsonr(temperaturas, consumos)
correlacion_spearman, p_spearman = spearmanr(temperaturas, consumos)

print("Correlación con Pearson:", correlacion_pearson)
print("Probabilidad Pearson:", p_pearson)

print("Correlación con Spearman:", correlacion_spearman)
print("Probabilidad Spearman:", p_spearman)