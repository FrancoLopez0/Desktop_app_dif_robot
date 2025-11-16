import serial

data = [[], [], [], []]
# data = []
sample_time = 0.1
stop_time_s = 10

len_max = int(stop_time_s/sample_time)

with serial.Serial('COM7', 9600, timeout=5) as ser:
    ser.write(b'm')
    while True:
        line = ser.readline()
        if not line:
            break
        print(line.decode("utf-8").strip())
        msg = line.decode("utf-8").strip()
        # if (msg == "Conectado"):
        #     break
        # try:
        #     data.append(float(msg))
        # except:
        #     pass
        splitted = line.decode("utf-8").strip().split(",")
        try:
            data[0].append(float(splitted[0]))
            data[1].append(float(splitted[1]))
            # data[2].append(float(splitted[2]))
            # data[3].append(float(splitted[3]))
        except:
            pass
        if (len(data[0]) > len_max):
            break

    ser.close()

print(data[0])

time = [sample_time*i for i in range(len(data[0]))]

with open("magnetometer_mx_my.csv", "w") as file:
    file.write("time,mx,my\n")
    for (r0, r1, r2) in zip(time, data[0], data[1]):
        file.write(str(r0) + ',' + str(r1) + ',' + str(r2) + "\n")
