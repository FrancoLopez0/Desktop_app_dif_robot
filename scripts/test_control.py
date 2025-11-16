import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import serial
import numpy as np
data_l = []
data_r = []
data_y = []
sample_time = 0.05
stop_time_s = 30

len_max = int(stop_time_s/sample_time)


def minimizar_en_grados(angulo):
    return (float(angulo) + 180) % 360 - 180


def minimizar_en_radianes(angulo):
    return (float(angulo) + np.pi) % (2 * np.pi) - np.pi


with serial.Serial('COM8', 9600, timeout=1) as ser:
    ser.write(b'8')
    # ser.write(b'a')
    while True:
        line = ser.readline()
        if not line:
            break
        raw_data = line.decode("utf-8").strip()
        print(raw_data)
        try:
            splitted = raw_data.split(",")
            data_l.append(float(splitted[0]))
            data_r.append(float(splitted[1]))
            # data_y.append(float(splitted[2]))
        except:
            pass
        if (len(data_r) > len_max or len(data_l) > len_max):
            break
    ser.close()

print(data_l, data_r)

time = [sample_time*i for i in range(len(data_r))]
set_point_0 = [1.6 for i in range(int(len(time)))]
set_point_1 = [1.8 for i in range(int(len(time)))]
set_point_2 = [1.3 for i in range(int(len(time)))]


def low_pass_filter(alpha, data: list):
    filtered_data = [data[0]]
    for i in range(1, len(data)):
        try:
            filtered_data.append(
                alpha * data[i] + (1 - alpha) * filtered_data[i - 1])
        except:
            pass
    return filtered_data


filtered_data = [low_pass_filter(
    0.041, data_l), low_pass_filter(0.03, data_r)]

# filtered_data = [list(map(minimizar_en_grados, filtered_data[0])), list(
#     map(minimizar_en_grados, filtered_data[1]))]

# Create a figure containing a single Axes.
# fig, ax = plt.subplots()
# ax.plot(time, np.rad2deg(data_l))
# ax.plot(time, data_r)
# ax.plot(time, data_y)

fig, ax = plt.subplots(2, 2, layout='constrained')

# ax[0].plot(time, data_l)
# ax[1].plot(time, data_r)

ax[0][0].plot(time, data_l)  # Plot some data on the Axes.
ax[1][0].plot(time, filtered_data[0])
# ax[1][0].plot(data_l, data_r)

ax[0][1].plot(time, data_r)  # Plot some data on the Axes.
ax[1][1].plot(time, filtered_data[1])

# ax[0][2].plot(time, data_y)
# ax[1][2].plot(data_r, data_y)
try:
    ax[0][0].plot(time, np.full_like(time, set_point_0), '--')
    ax[0][1].plot(time, np.full_like(time, set_point_0), '--')
    ax[1][0].plot(time, np.full_like(time, set_point_0), '--')
    ax[1][1].plot(time, np.full_like(time, set_point_0), '--')
    ax[0][0].plot(time, np.full_like(time, set_point_1), '--')
    ax[0][1].plot(time, np.full_like(time, set_point_1), '--')
    ax[1][0].plot(time, np.full_like(time, set_point_1), '--')
    ax[1][1].plot(time, np.full_like(time, set_point_1), '--')
    ax[0][0].plot(time, np.full_like(time, set_point_2), '--')
    ax[0][1].plot(time, np.full_like(time, set_point_2), '--')
    ax[1][0].plot(time, np.full_like(time, set_point_2), '--')
    ax[1][1].plot(time, np.full_like(time, set_point_2), '--')

except:
    pass

plt.show()                           # Show the figure.
