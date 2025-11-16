import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from pandas import read_csv

# Datos de entrada (voltaje aplicado) y salida (velocidad medida)

df = read_csv("lazo_abierto_motores.csv")
data = df.values

output = df['vel_r']  # Velocidad
input = np.array([767 for i in range(np.size(output))])  # Voltaje

print(input)

# Supongamos que el sistema se comporta como un sistema de primer orden


def modelo_primer_orden(t, K, tau):
    return K * (1 - np.exp(-t / tau))


# Ajustar el modelo a los datos experimentales
t = np.arange(len(output))  # Tiempo en unidades discretas
parametros, _ = curve_fit(modelo_primer_orden, t, output, p0=[1, 1])

# Parámetros ajustados
K_ajustado, tau_ajustado = parametros
print(f"Ganancia K: {K_ajustado}, Tiempo de constante tau: {tau_ajustado}")

# Parámetro lambda (ajústalo según el comportamiento deseado)
lambda_val = 0.2*tau_ajustado
# lambda_val = 1.14
# Parámetros de la planta (obtenidos a partir de la identificación)
K = K_ajustado  # Ganancia estática
tau = tau_ajustado  # Constante de tiempo

# Calcular los parámetros del controlador PID
# Kp = lambda_val * (1 / K)
Kp = tau / (K * lambda_val)
Ki = Kp / tau
Kd = 0
# Kd = lambda_val * (tau / 2)  # T_d = tau / 2 es un valor común

print(f"PID Parameters: Kp = {Kp}, Ki = {Ki}, Kd = {Kd}")

# Graficar el ajuste
output_ajustada = modelo_primer_orden(t, K_ajustado, tau_ajustado)
plt.plot(t, output, label='Datos experimentales')
plt.plot(t, output_ajustada, label='Modelo ajustado', linestyle='dashed')
plt.legend()
plt.show()
