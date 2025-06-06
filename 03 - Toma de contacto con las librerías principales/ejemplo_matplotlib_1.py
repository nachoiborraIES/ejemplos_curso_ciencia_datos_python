# Ejemplos de gráficos simples con Matplotlib

import matplotlib.pyplot as plt

# Gráfico de líneas
x = [1, 2, 3, 4, 5]
y = [2, 8, 4, 7, 9]
plt.plot(x, y)
plt.show()

# Gráfico de dispersión con mismos valores de x e y
plt.scatter(x, y)
plt.show()