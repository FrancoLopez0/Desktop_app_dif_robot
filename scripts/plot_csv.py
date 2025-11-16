import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# def men_360(data):
#     while (data >= 360):
#         data -= 360
# Función para minimizar un ángulo en grados en el rango (-180°, 180°]
def minimizar_en_grados(angulo):
    return (angulo + 180) % 360 - 180

# Función para minimizar un ángulo en radianes en el rango (-π, π]


def minimizar_en_radianes(angulo):
    return (angulo + np.pi) % (2 * np.pi) - np.pi


def filtro_media_movil(signal, N):
    """
    Aplica un filtro de media móvil a una señal.

    Args:
        signal (list or np.array): La señal de entrada.
        N (int): El tamaño de la ventana del filtro (número de muestras a promediar).

    Returns:
        np.array: La señal filtrada.
    """
    # Verificar que N sea un número positivo
    if N <= 0:
        raise ValueError(
            "El tamaño de la ventana N debe ser un número positivo.")

    # Crear el filtro de media móvil
    filtro = np.ones(N) / N  # Un filtro de N elementos con valor 1/N
    # Aplicar la convolución para obtener la señal filtrada
    filtered_signal = np.convolve(signal, filtro, mode='same')

    return filtered_signal


def low_pass_filter(alpha, data):
    filtered_data = [data[0]]
    for i in range(1, len(data)):
        filtered_data.append(
            alpha * data[i] + (1 - alpha) * filtered_data[i - 1])
    return filtered_data


df = pd.read_csv('csv\magnetometer_mx_my.csv', sep=',')

# df['orientation'] = np.rad2deg(df['orientation'])

# df['orientation'] = [while () for item in df['orientation']]

mx = df['mx'].to_numpy()
my = df['my'].to_numpy()

min_x =min(mx)
max_x =max(mx)
min_y =min(my)
max_y =max(my)

bias_x =(max_x + min_x)/2
delta_x = (max_x - min_x)/2

bias_y =(max_y + min_y)/2
delta_y = (max_y - min_y)/2

delta_avg = (delta_y+delta_x)/2

scale_x = delta_avg / delta_x
scale_y = delta_avg / delta_y


mx_calibrated = scale_x * (mx - bias_x)
my_calibrated = scale_y * (my - bias_y)

# df['orientation'] = np.rad2deg(df['orientation'])

# df['orientation'] = list(map(minimizar_en_grados, df['orientation']))

# filtered_data = low_pass_filter(0.004117, df['orientation'].to_list())
# media_movil = filtro_media_movil(df['orientation'], 5)
# # ation'].to_list())
# media_movil = filtro_media_movil(df['orientation'], 5)

# ref = 45

transformation = []

# for item in df['orientation']:
#     n = item - ref + 90
#     # if item < ref and item > -180:
#     #     item = n + 180

#     transformation.append(n)
# # df['orientation'] = filtered_data

# df.to_csv('data_l_start_duty_non_filtered_pilas_nuevas.csv', index=False)

# df.plot(x='time', y='orientation')
fig, ax = plt.subplots(2, 1, layout='constrained')

ax[0].set_title("Magnetometro no calibrado")
ax[0].plot(df['time'], df['mx'], label='mx')
ax[0].plot(df['time'],df['my'], label='my')
ax[0].legend()
ax[0].set_xlabel("Tiempo")
ax[0].set_ylabel("Magnetometro")

ax[1].set_title("Magnetometro calibrado")
ax[1].plot(df['time'],mx_calibrated, label='mx')
ax[1].plot(df['time'],my_calibrated, label='my')
ax[1].legend()
ax[1].set_xlabel("Tiempo")
ax[1].set_ylabel("Magnetometro")
# ax[1].plot(df['time'], transformation)
# ax[1].plot(df['time'], [0 for i in range(len(df['time']))])
# ax[2].plot(df['time'], media_movil)

plt.show()
