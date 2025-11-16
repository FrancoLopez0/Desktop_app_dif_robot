import numpy as np

class KalmanFilter:
    def __init__(self, dt):
        # Inicialización de matrices para el filtro de Kalman
        # Estado [x, y, theta]
        self.dt = dt

        self.x = np.zeros((3, 1))  # [x, y, theta]

        # Matrices de covarianza
        self.P = np.eye(3) * 1000  # Inicialización con una alta incertidumbre

        # Matriz de transición de estado
        self.F = np.eye(3)

        # Matrices de control (velocidades v y omega)
        self.B = np.array([[np.cos(self.x[2]) * dt, 0],
                           [np.sin(self.x[2]) * dt, 0],
                           [0, dt]])

        # Ruido de proceso (puedes ajustar estos valores según el sistema)
        self.Q = np.eye(3) * 0.01

        # Matriz de medición
        self.H = np.eye(3)

        # Ruido de medición (ajustar según los sensores)
        self.R = np.eye(3) * 0.1

    def predict(self, v, omega):
        # Predicción del estado basado en el modelo de movimiento
        self.F[0, 2] = -np.sin(self.x[2]) * v * self.dt  # Cambio de x debido a theta
        self.F[1, 2] = np.cos(self.x[2]) * v * self.dt  # Cambio de y debido a theta

        u = np.array([[v], [omega]])  # Velocidades controladas (lineales y angulares)

        # Predicción del siguiente estado
        self.x = self.x + np.dot(self.B, u)

        # Predicción de la covarianza
        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q

    def update(self, z):
        # Actualización del filtro con nuevas mediciones (posiciones del robot)
        y = z - np.dot(self.H, self.x)  # Residual de la medición
        S = np.dot(np.dot(self.H, self.P), self.H.T) + self.R  # Covarianza de la medición
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))  # Ganancia de Kalman

        # Actualización del estado
        self.x = self.x + np.dot(K, y)

        # Actualización de la covarianza
        self.P = np.dot(np.eye(3) - np.dot(K, self.H), self.P)

    def get_state(self):
        return self.x

# # Parámetros del robot
# dt = 0.1  # Intervalo de tiempo
# v = 0.5   # Velocidad lineal (m/s)
# omega = 0.1  # Velocidad angular (rad/s)

# # Inicializar el filtro de Kalman
# kf = KalmanFilter(dt)

# # Simulación de un ciclo de predicción y actualización
# for _ in range(100):
#     # Predicción
#     kf.predict(v, omega)
    
#     # Simulación de una medición de posición (esto debería venir de un sensor real)
#     z = kf.get_state() + np.random.normal(0, 0.1, (3, 1))  # Simulación de ruido en las mediciones
    
#     # Actualización con la medición
#     kf.update(z)
    
#     # Obtener la posición estimada
#     estimated_position = kf.get_state()
#     print(f"Posición estimada: {estimated_position.flatten()}")
