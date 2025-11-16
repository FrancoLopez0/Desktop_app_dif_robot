from PySide6.QtCore import QThread, Signal
import time
from random import randint


class SerialReaderThread(QThread):
    # Señal centralizada que pasa los datos a todos los gráficos

    new_data = Signal(int, name='new_data')

    def __init__(self, serial_port='COM8', baud_rate=9600):
        super().__init__()
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        # self.ser = serial.Serial(self.serial_port, self.baud_rate)

    def run(self):
        while True:
            time.sleep(0.01)
            self.new_data.emit(randint(0, 100))
            # if self.ser.in_waiting > 0:
            #     try:
            #         # Leer el dato desde el puerto serial
            #         data = float(self.ser.readline().decode('utf-8').strip())
            #         # Emitir la señal con el nuevo dato
            #         self.new_data_signal.emit(data)
            #     except ValueError:
            #         # Si el dato no es válido, ignorarlo
            #         pass

            # def close(self):
            #     if self.ser.is_open:
            #         self.ser.close()
