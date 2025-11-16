import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores para x e y
x_min, x_max = -5, 5
y_min, y_max = -5, 5
n_points = 20  # Número de puntos en cada eje

# Crear una malla de puntos en el plano
x = np.linspace(x_min, x_max, n_points)
y = np.linspace(y_min, y_max, n_points)
X, Y = np.meshgrid(x, y)

# Definir los valores constantes Posicion_x y Posicion_y
Posicion_x, Posicion_y = 0, 0  # Puedes cambiar estos valores

# Calcular el ángulo theta en cada punto
theta = np.arctan2(Posicion_y-Y, Posicion_x - X)

# Calcular los componentes del campo vectorial
Vx = np.cos(theta)
Vy = np.sin(theta)

# Graficar el campo vectorial
plt.figure(figsize=(6,6))
plt.quiver(X, Y, Vx, Vy, scale=20, color='b')
plt.scatter(Posicion_x, Posicion_y, color='r', marker='o', label='Fuente')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Campo Vectorial de atan2(y - Posicion_y, x - Posicion_x)")
plt.legend()
plt.grid()
plt.show()
