# This Python file uses the following encoding: utf-8
import sys
import time
import numpy as np
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QVBoxLayout, QLabel, QDialog
# ,pyqtSignal, QVBoxLayout
from PySide6.QtCore import QTimer, QThread, Signal, Slot, Qt, QSize
import pyqtgraph as pg
from models import Robot
# import models.KalmanFilter
import scripts
import copy
from random import randint
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
import scripts.scripts
from models import Loading
import serial
from collections import deque
from ui_form import Ui_MainWindow
from pyqtgraph import PlotWidget

SCALE_FACTOR = 10000
is_referenced_from_robot = False
waiting_instructions = False

def R_inv(theta) -> np.array:
    return np.array([[np.cos(theta), np.sin(theta)],
                    [-np.sin(theta), np.cos(theta)]])

def R_inv_Transform(point:list,theta:float):
    return np.dot(R_inv(theta),np.array(point))

def Rot(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                [np.sin(theta), np.cos(theta)]])

def R_Transform(point:list, theta:float):
    return np.dot(Rot(theta), np.array(point))

class RealTimePlotWidget(PlotWidget):
    def __init__(self, max_points: int = 100, margin: int = 10, plot: PlotWidget = None):
        super().__init__()

        self.max_points = max_points
        self.margin = margin
        self.plot_object = plot
        self.save_data = False
        self.stop_save_data = False
        self.data_csv = []
        # # Crear la curva que se actualizará con los datos
        # self.plot(pen='y')
        self.x_axis = []
        self.y_axis = []
        self.theta = 0
        # Inicializar los datos (con deque para mantener solo los últimos puntos)
        self.data = deque(maxlen=self.max_points)
        self.time = deque(maxlen=self.max_points)
        self.timer_counter = 0
        self.ant_timer_value = self.timer_counter
    
    def set_azimuth(self, theta):
        self.theta = theta
    
    def get_azimuth(self):
        return self.theta

    def draw_point(self, x, y, symbol = 'o', size=10, color = 'r'):
        self.plot_object.plot([x], [y], pen=None, symbol='o', symbolSize=10, symbolBrush=color)

    def draw(self, x, y):
        # self.plot_object.clear()
        self.plot_object.plot(x, y)

    def draw_arrow(self, angle, origin):
        arrow = pg.ArrowItem(pos=origin, angle=angle, tipAngle=30, baseAngle=0, tailWidth=5)
        self.plot_object.addItem(arrow)
        return

    def clear_plt(self):
        self.x_axis.clear()
        self.y_axis.clear()
        self.plot_object.clear()

    def update_plot(self, data):
        # self.data_csv.append([data[0],data[1]])
        # print(data)

        if(len(data)>=4):
            x = float(data[1])
            y = float(data[2])
            angle = float(data[3]) + 90
            point = [x,y]
            if(is_referenced_from_robot):
                point = R_Transform(point, self.theta)
            x = point[0]
            y = point[1]
            print(x, y)
            self.x_axis.append(x) 
            self.y_axis.append(y)
            self.draw(self.y_axis,self.x_axis)
            self.draw_point(float(data[5]),float(data[4]),color='g')
            self.draw_arrow(angle,(y,x))
        # self.time.append(self.timer_counter)
        # self.data.append(data)
        # if self.save_data:
        #     self.data_csv.append([self.timer_counter, data])
        #     if self.stop_save_data:
        #         self.save_data = False
        #         self.stop_save_data = False
        #         scripts.scripts.save_csv(self.data_csv, "data.csv")
        #         self.data_csv = []
        # self.draw(list(self.time), list(self.data))
        # self.timer_counter += 1

        # print(f"Deque: {len(self.data)}")
        # if self.timer_counter > self.ant_timer_value + 100:
        #     self.ant_timer_value = self.timer_counter

        # self.plot_object.setXRange(
        #     self.timer_counter - 100, self.timer_counter)

        # self.setXRange(
        #     self.timer_counter - 100, self.timer_counter)

class SerialReaderThread(QThread):
    # Señal centralizada que pasa los datos a todos los gráficos

    connecting = Signal(str, name='connecting')
    new_data = Signal(int, name='new_data')
    new_list = Signal(list, name='new list')
    new_coords = Signal(list, name='new coords')
    new_text_to_show = Signal(str, name='new text to show')
    new_theta = Signal(float, name='new theta')
    new_serial_data = Signal(str, name='new serial data')
    signal_in_position = Signal(str, name = 'in position')
    magnetometer_data = Signal(list, name = 'magnetometer data')
    set_values_to_calibrate_magnetometer = Signal(list, name='set values to calibrate magnetometer')

    def __init__(self):
        super().__init__()
        self.ser = None
        self.baud_rate = 9600
        self.port = 'COM6'
        self.haveData = False
        self.x = 0
        self.y = 0
        self.in_position = False
        self.moving = False
        self.calibrate_mode = False
        self.square = [[0,90],[90,90],[90,0],[0,0]]
        # self.baud_rate = baud_rate
        # self.ser = serial.Serial(self.serial_port, self.baud_rate)
    
    def set_port(self, port):
        self.port = port
    
    def set_baud_rate(self, baud_rate):
        self.baud_rate = baud_rate

    def init_com(self):
        
        try:
            self.connecting.emit("Connecting")
            self.ser = serial.Serial(self.port, self.baud_rate)

            self.connecting.emit("Connected")

            return True
        except:
            print("ERROR")
            self.connecting.emit("Fail")
            return False


    def run(self):
        if self.init_com():
            while True:
                # time.sleep(0.01)
                # self.new_data.emit(randint(0, 100))
                if self.ser is not None:
                    if self.ser.in_waiting > 0:
                        # try:
                        #     # Leer el dato desde el puerto serial

                        #     data = float(
                        #         self.ser.readline().decode('utf-8').strip())
                        #     # Emitir la señal con el nuevo dato
                        #     self.new_data.emit(data)

                        # except ValueError:
                        try:
                            data = self.ser.readline().decode('utf-8').strip()
                            self.haveData = True
                            self.new_serial_data.emit(data)
                            data = data.split(',')
                            # print(data)
                            waiting_instructions = False

                            if(data[0]=='/'):
                                self.new_coords.emit(data)
                            
                            if(data[0]=='theta'):
                                self.new_theta.emit(float(data[1]))

                            if(data[0]=='fpos'):
                                future_position = str(int(round(self.x,0))) + ',' + str(int(round(self.y,0))) + '\r'
                                time.sleep(0.250)
                                self.ser.write(future_position.encode('utf-8'))
                                print(future_position)
                            
                            if(data[0]=='on_pos'):
                                self.moving = False
                                self.signal_in_position.emit("in position")

                            if(data[0]=='m'):
                                print(data[1],data[2])
                                self.magnetometer_data.emit([float(data[1]),float(data[2])])

                            if(data[0]=='s_v_mag'):
                                self.set_values_to_calibrate_magnetometer.emit([])

                            if(data[0]=='+'):
                                print("Esperando instrucciones")
                                waiting_instructions = True
                        except:
                            # print(data)
                            pass
                        # if(data == '/'):#Al recibir el caracter '/' indico que se enviara un csv de columnas x, y
                        #     self.new_text_to_show.emit('Coords')
                        #     while True:
                        #         data = self.ser.readline().decode('utf-8').strip()
                        #         print(data)
                        #         if(data == '+'):#Al recibir el caracter '+' termina el envio del csv
                        #             break
                        #         data = data.split(',')
                        #         self.new_coords.emit(data)
                        # self.new_text_to_show.emit(data)
                            # Si el dato no es válido, ignorarlo


    def close(self):
        if self.ser.is_open:
            self.ser.close()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Robot App")
        self.robot = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.hay_un_siguiente_punto = False
        self.square_index = 0
        self.is_connected = False
        self.move_square = [[0,90],[90,90],[90,0],[0,0]]
        self.points = []
        
        # self.kalmanFilter = models.KalmanFilter.KalmanFilter(0.05)
        # THREADS
        # Crear el hilo que se encargará de leer los datos del puerto serial
        self.serial_thread = SerialReaderThread()
        self.robot = Robot.Robot()
        # COMBO BOXES
        self.ui.cbSelectBaudRate.addItems(['9600', '115200'])

        # MENU
        self.ui.pbtnConnect.clicked.connect(self.connect)
        # self.ui.pbtnConnect_2.connect(self.serial_thread.ser.close)
        self.ui.pbScanPorts.clicked.connect(self.scan_ports)
        self.ui.btnCalibrate.clicked.connect(self.calibrate)
        self.ui.btnTestMotors.clicked.connect(self.test_motors)
        self.ui.btnGoToPos.clicked.connect(self.go_to_pos)
        self.ui.btnTestControl.clicked.connect(self.get_magnetometer_data)
        self.ui.btnUploadControl.clicked.connect(self.set_pid_params)
        self.ui.btnAddPoint.clicked.connect(self.add_point)
        self.ui.btnClearTab.clicked.connect(self.clear_tab)
        self.ui.btnSetDistanceError.clicked.connect(self.set_distance_error)
        self.ui.btnRun.clicked.connect(self.go_to_points)

        # SERIAL COMMUNICATION
        self.ui.pbtnSendSerial.clicked.connect(self.send_serial)
        # GRAPH
        self.ui.graphBig.setRange(xRange=[-100, 100], yRange=[-100, 100])
        self.ui.graphBig.showGrid(x = True, y = True)
        self.ui.graphBig.scene().sigMouseClicked.connect(self.get_mouse_pos)
        polarPlot = pg.PlotDataItem(pen='r', symbol='o')
        arrow = pg.ArrowItem(pos=(0,0), angle=90, tipAngle=30, baseAngle=30, tailWidth=10)
        self.ui.graphOrientation.addItem(arrow)
        self.ui.graphOrientation.hideAxis('left')
        self.ui.graphOrientation.hideAxis('bottom')
        self.ui.graphOrientation.setRange(xRange=[-10,10], yRange=[-10,10])

        self.graphVel1 = RealTimePlotWidget(
            margin=10, max_points=100, plot=self.ui.graphBig)

        self.serial_thread.new_coords.connect(self.new_coords)
        self.serial_thread.new_text_to_show.connect(self.ui.serialInput.setPlainText)
        self.serial_thread.new_theta.connect(self.graphVel1.set_azimuth)
        self.serial_thread.new_serial_data.connect(self.show_serial_data)
        self.serial_thread.signal_in_position.connect(self.in_position)
        self.serial_thread.magnetometer_data.connect(self.robot.set_values_to_calibrate_magnetometer)
        self.serial_thread.set_values_to_calibrate_magnetometer.connect(self.set_magnetometer_calibration_values)
        
        self.ui.tabPointsToGo.setColumnCount(2)
        self.ui.tabWidget.setTabText(0,'Position')
        self.ui.tabWidget.setTabText(1,'CRN')
        self.ui.tabWidget.setTabText(2,'Params')
        
        self.loading_dialog = Loading.LoadingDialog("assets\walking_robot.gif", "Loading...")
        self.serial_thread.connecting.connect(self.loading_connect_serial)

        self.dialog = Loading.Dialog("Robot App")

        self.ui.tabWidget.removeTab(1)

        # VARIABLES
        self.data_x = deque(maxlen=100)
        self.data_y = deque(maxlen=100)
        self.timer_counter = 0
        self.ant_timer_value = self.timer_counter

        self.qty_points = 0
        self.points_to_go_x = []
        self.points_to_go_y = []

    def set_state_set_calibration_values_magnetometer(self, data):
        self.send_serial_str("y")

    def set_magnetometer_calibration_values(self, data):
        list_truncated = list(map(lambda num: f"{num:.4f}", self.robot.magnetometer.get_params_to_calibrate()))
        string = ",".join(map(str, list_truncated))
        print(string)
        self.send_serial_str(string)

    def enable_btns(self):
        self.ui.btnCalibrate.setEnabled(True)
        self.ui.btnTestControl.setEnabled(True)
        self.ui.btnGoToPos.setEnabled(True)
        self.ui.btnTestControl.setEnabled(True)
        self.ui.btnTestMotors.setEnabled(True)

    def disable_btns(self):
        self.ui.btnCalibrate.setEnabled(False)
        self.ui.btnTestControl.setEnabled(False)
        self.ui.btnGoToPos.setEnabled(False)
        self.ui.btnTestControl.setEnabled(False)
        self.ui.btnTestMotors.setEnabled(False)

    def loading_connect_serial(self, load):
        if self.loading(load)=="Connected":
            self.enable_btns()
            self.ui.serialInput.setPlainText(
                f"Conectado a {self.serial_thread.port} / {self.serial_thread.baud_rate} bauds")
            self.ui.pbtnConnect.setText("Disconnect")
            self.is_connected = True
        if self.loading(load)=="Fail":
            self.ui.serialInput.setPlainText(f"No se pudo conectar a {self.serial_thread.port} / {self.serial_thread.baud_rate} bauds")

    def loading(self, load):
        if(load == "Connecting"):
            self.init_loading()
            return load
        if(load == "Connected"):
            self.close_loading()
            return load
        if(load == "Fail"):
            self.close_loading()
            self.dialog.set_text("Error")
            self.dialog.show()
            QTimer.singleShot(1500, self.dialog.close)
            return False

    def init_loading(self):
        self.loading_dialog.show()

    def new_coords(self,data):
        data = np.array(data)
        data = data.tolist()
        self.graphVel1.update_plot(data)
        arrow = pg.ArrowItem(pos=(0,0), angle=180 - float(data[7]), tipAngle=30, baseAngle=0, tailWidth=5)
        self.ui.graphOrientation.clear()
        self.ui.graphOrientation.addItem(arrow)
        return

    def set_state_go_to_pos(self):
        self.serial_thread.ser.write(b'4')  
        return

    def set_destiny_position(self,pos:list):
        self.serial_thread.x = pos[0]
        self.serial_thread.y = pos[1]
        return

    def add_point_to_go(self, point:list):
        self.points.append([point])
        return

    def in_position(self, data):
        
        if(self.points):
            self.set_destiny_position(self.points[1])
            self.points.pop(0)
            self.set_state_go_to_pos()
            time.sleep(1)
            if(len(self.points) == 1):
                self.points.clear()

        return

    def set_distance_error(self):
        self.serial_thread.ser.write(b'e')

        time.sleep(.2)
        distance_error = self.ui.sbDistanceError.value()
        distance_error = str(distance_error)+'\r'
        distance_error = distance_error.encode('utf-8')
        self.serial_thread.ser.write(bytes(distance_error))
        print(distance_error)
        return

    def get_params(self):
        self.serial_thread.ser.write(b'p')
        time.sleep(0.2)
        orientation = self.graphVel1.get_azimuth()
        self.ui.tabParams.setItem(0,1,QTableWidgetItem(str(orientation)))

    def keyPressEvent(self, event):
        # Capturar la tecla presionada
        key = event.key()
        
        # Mostrar el código de la tecla presionada
        if key == Qt.Key_Escape:
            self.close()  # Cerrar la aplicación cuando se presiona Esc
        elif key == Qt.Key_Enter:
            self.go_to_pos()
        elif key == Qt.Key_A:
            self.add_point()
        elif key == Qt.Key_C:
            self.clear_tab()
        else:
            # Si es otra tecla, mostrar el código de la tecla presionada
            self.label.setText(f"Tecla presionada: {chr(key)}")

    def clear_tab(self):
        self.ui.tabPointsToGo.clear()
        self.graphVel1.clear_plt()
        self.points_to_go_x.clear()
        self.points_to_go_y.clear()
        self.points.clear()
        self.qty_points = 0
        return

    def add_point(self):
        
        row_pos = self.qty_points
        # if(row_pos < 5):
        # self.ui.tabPointsToGo.insertRow(row_pos)
        x = self.ui.x_pos_robot.value()
        y = self.ui.y_pos_robot.value()
        self.ui.tabPointsToGo.setItem(row_pos,0,QTableWidgetItem(str(x)))
        self.ui.tabPointsToGo.setItem(row_pos,1,QTableWidgetItem(str(y)))
        if(len(self.points_to_go_x)<5):
            self.points.append([y,x])   
            self.points_to_go_x.append(x)
            self.points_to_go_y.append(y)
            self.qty_points+=1

        print(f'points: {self.points}')
        return
    
    def load_points_to_go(self, points):
        self.points = copy.deepcopy(points)
        return

    def get_mouse_pos(self, event):
        # Obtener la posición del clic
        pos = event.scenePos()
        
        vb = self.ui.graphBig.geometry()
        min_x = 80
        max_x = 516
        min_y = 40
        max_y = 416
        if(pos.x()>min_x and pos.y()>min_y and pos.x()<max_x and pos.y()<max_y):
            pos_x = (pos.x()-min_x)/(max_x-min_x)*200 - 100
            pos_y = 100 - (pos.y()-min_y)/(max_y-min_y)*200

            self.ui.x_pos_robot.setValue(int(pos_x))
            self.ui.y_pos_robot.setValue(int(pos_y))
            
            self.graphVel1.clear_plt()
            self.graphVel1.draw_point(pos_x,pos_y)
            
            for x,y in zip(self.points_to_go_x, self.points_to_go_y):
                self.graphVel1.draw_point(x,y,color='g')
        

    def show_serial_data(self, data):
        self.ui.serialInput.appendPlainText(data)
        return

    def set_pid_params(self):
        self.serial_thread.ser.write(b'c')

        kp = int(self.ui.sboxKp.value() * 10000)
        kd = int(self.ui.sboxKd.value() * 10000)
        
        kd = bytes(str(kd).encode('utf-8'))+ b'\r'
        kp = bytes(str(kp).encode('utf-8')) + b'\r'
        
        kp = kp
        kd = kd
       
        print(kp,kd)

        time.sleep(0.5)
        self.serial_thread.ser.write(kp)
        time.sleep(0.5)
        self.serial_thread.ser.write(kd)     
        # time.sleep(0.1)
        # self.serial_thread.ser.write(b' ')
        return

    def closeEvent(self, event):
        # Asegurarse de cerrar el hilo y el puerto serial cuando se cierre la ventana
        self.serial_thread.terminate()
        event.accept()

    def go_to_points(self):

        self.load_points_to_go(self.points)

        self.set_destiny_position(self.points[0])

        self.set_state_go_to_pos()

        return

    def calibrate(self):

        self.load_points_to_go(self.move_square)

        self.set_destiny_position(self.move_square[0])

        self.set_state_go_to_pos()

        return

    def test_motors(self):
        self.serial_thread.ser.write(b'2')
        return
    
    def send_serial_str(self,txt):
        self.serial_thread.ser.write(b',' + bytes(txt.encode("utf-8")) + b'\r')

    def go_to_pos(self):

        self.set_pid_params()

        self.graphVel1.clear_plt()
        self.serial_thread.ser.write(b'4')
        self.serial_thread.x = self.ui.x_pos_robot.value()
        self.serial_thread.y = self.ui.y_pos_robot.value()
        self.graphVel1.draw_point(self.serial_thread.y,self.serial_thread.x)

        return

    def get_magnetometer_data(self):
        self.serial_thread.ser.write(b'm')
        return

    def scan_ports(self):
        self.ui.cbSelectCom.clear()
        # self.loading_dialog = LoadingDialog("assets\walking_robot.gif", "Scanning")
        # self.loading_dialog.show()

        # Simular una tarea de carga en segundo plano
        # QTimer.singleShot(3000, self.close_loading)
        self.ui.cbSelectCom.addItems(scripts.scripts.list_ports())
        self.ui.pbtnConnect.setEnabled(True)
        return

    def close_loading(self):
        self.loading_dialog.close()

    def connect(self):
        port = self.ui.cbSelectCom.currentText()
        baud_rate = self.ui.cbSelectBaudRate.currentText()
        if not self.is_connected:
            try:
                self.serial_thread.set_port(port)
                self.serial_thread.set_baud_rate(baud_rate)
                self.serial_thread.start()
            except:
                return
        else:
            self.serial_thread.close()
            self.ui.pbtnConnect.setText("Connect")
            self.disable_btns()
            self.is_connected = False
        

    def send_serial(self):
        data = self.ui.txtMsgToSend.toPlainText()
        self.serial_thread.ser.write(data.encode("utf-8"))
        return

    def continue_script(self):
        self.serial_thread.ser.write(b'1')
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
