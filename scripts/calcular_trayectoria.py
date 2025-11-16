import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumulative_trapezoid
import math

sample_time = 0.1
radius_wheel_cm = 3
distance_btwn_wheels = 13.2

df = pd.read_csv("velocities_t_3.csv")

vel_wheel_l_rpm = np.array(df['vel_l'])
vel_wheel_r_rpm = np.array(df['vel_r'])

time = np.array(df['time'])

vel_robot_t = (vel_wheel_r_rpm + vel_wheel_l_rpm) * radius_wheel_cm/2

angular_velocity_robot = (vel_wheel_r_rpm - vel_wheel_l_rpm) * \
    radius_wheel_cm / distance_btwn_wheels

# robot_orientation = [(angular_velocity_robot[i] - angular_velocity_robot[i-1]) /
#                      (time[i]-time[i-1]) for i in range(1, len(angular_velocity_robot))]

# robot_orientation = np.array(robot_orientation)

robot_orientation = cumulative_trapezoid(angular_velocity_robot, time)

vel_robot_t = vel_robot_t[:-1]

vel_robot_t_vector_x = vel_robot_t * np.cos(robot_orientation)

vel_robot_t_vector_y = vel_robot_t * np.sin(robot_orientation)

# pos_x = [(vel_robot_t_vector_x[i]-vel_robot_t_vector_x[i-1]) /
#          sample_time for i in range(1, len(vel_robot_t_vector_x))]

pos_x = cumulative_trapezoid(vel_robot_t_vector_x, time[:-1])
pos_y = cumulative_trapezoid(vel_robot_t_vector_y, time[:-1])

fig, ax = plt.subplots(2, 2)

ax[0][0].plot(time[:-1], vel_robot_t, 'o')
ax[0][0].set_title("Velocity")
ax[0][0].set_xlabel("time(s)")
ax[0][0].set_ylabel("velocity(cm/s)")

ax[0][1].plot(time[:-1], np.rad2deg(robot_orientation))
ax[0][1].set_title("Orientation")
ax[0][1].set_xlabel("time(s)")
ax[0][1].set_ylabel("orientation(degrees)")

ax[1][0].plot(time[:-2], pos_x, label="x position")
ax[1][0].plot(time[:-2], pos_y, label="y position")
ax[1][0].set_title("Position")
ax[1][0].set_xlabel("position(cm)")
ax[1][0].set_ylabel("time(s)")
ax[1][0].legend()

ax[1][1].plot(pos_x, pos_y)
ax[1][1].set_title("Trajectory")
ax[1][1].set_xlabel("pos x(cm)")
ax[1][1].set_ylabel("pos y(cm)")

plt.show()
print(max(pos_x), min(pos_x))
