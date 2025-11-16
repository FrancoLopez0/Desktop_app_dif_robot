import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

K = 70.40700318854658
Kp = 0.007101566283982063
Ki = 0.0002884017578995638
Kd = 6.155966537533373

tau = 24.62386615013349

# Función de transferencia de la planta (modelo obtenido anteriormente)
num = [K]  # Numerador
den = [tau, 1]  # Denominador
plant = ctrl.TransferFunction(num, den)

# Controlador PID (de acuerdo con los parámetros calculados)
PID = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])

# Sistema en lazo cerrado (retroalimentado)
closed_loop_system = ctrl.feedback(PID * plant)

# Simulación de la respuesta al escalón
t = np.linspace(0, 10, 1000)  # Tiempo de simulación
t, y = ctrl.step_response(closed_loop_system, t)

# Graficar la respuesta
plt.plot(t, y)
plt.title("Respuesta del Sistema con Controlador PID (Sintonización Lambda)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidad [rpm]")
plt.grid(True)
plt.show()
