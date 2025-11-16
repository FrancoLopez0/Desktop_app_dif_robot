# import numpy as np
# from math import atan
# xd = 100
# yd = 100

# orientacion_actual = 2

# theta = 1.5707963267948966 - orientacion_actual

# xd_respecto_del_norte = xd*np.cos(theta) + yd*np.sin(theta)
# yd_respecto_del_norte = - xd*np.sin(theta) + yd*np.cos(theta)

# theta_deseado = np.atan2(yd_respecto_del_norte, xd_respecto_del_norte)

# xd = xd_respecto_del_norte * \
#     np.cos(theta_deseado) - yd_respecto_del_norte * np.sin(theta_deseado)

# yd = xd_respecto_del_norte * \
#     np.sin(theta_deseado) + yd_respecto_del_norte * np.cos(theta_deseado)

# print(theta_deseado, xd, yd)

import numpy as np
import matplotlib.pyplot as plt
# Coordenadas originales
xd = 0
yd = 90

robto_pos = [-0.718310, 2.526730]
init_angle = 1.845659

# Ángulo de rotación (en radianes)
theta = np.pi/2 - init_angle  # 45 grados

def R_inv(theta) -> np.array:
    return np.array([[np.cos(theta), np.sin(theta)],
                    [-np.sin(theta), np.cos(theta)]])

def R_inv_Transform(point:list,theta:float):
    return np.dot(R_inv(theta),np.array(point))

def Rot(theta):
    R = np.array([[np.cos(theta), -np.sin(theta)],
                [np.sin(theta), np.cos(theta)]])

def R_Transform(point:list, theta:float):
    return np.dot(Rot(theta), np.array(point))

# Matriz de rotación R(theta)
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])

# Matriz inversa de rotación R^(-1)(theta)
R_inv = np.array([[np.cos(theta), np.sin(theta)],
                  [-np.sin(theta), np.cos(theta)]])

# Vector de coordenadas original
vector_original = np.array([xd, yd])

# Aplicar rotación y luego la inversa
vector_rotado = R_Transform(np.array([10,10]),90)#np.dot(R_inv, vector_original)  # Rotación
vector_reconvertido = np.dot(R, vector_rotado)  # Inversa de la rotación

# Imprimir resultados
print(f"Coordenadas originales: {vector_original}")
print(f"Coordenadas después de la rotación: {vector_rotado}")
# print(f"Coordenadas después de aplicar la inversa: {vector_reconvertido}")

fig, ax = plt.subplots(2, 1)
ax[0].quiver(0, 0, vector_original[0], vector_original[1],
             angles='xy', scale_units='xy', scale=1)
ax[1].quiver(0, 0, vector_rotado[0], vector_rotado[1],
             angles='xy', scale_units='xy', scale=1)
ax[1].quiver(0, 0, robto_pos[0], robto_pos[1],
             angles='xy', scale_units='xy', scale=1)
ax[0].plot(vector_original[0], vector_original[1], 'ro')
ax[1].plot(vector_rotado[0], vector_rotado[1], 'ro')
ax[1].plot(robto_pos[0], robto_pos[1])
plt.show()
