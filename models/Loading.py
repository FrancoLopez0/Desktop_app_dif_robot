from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QVBoxLayout, QLabel, QDialog
# ,pyqtSignal, QVBoxLayout
from PySide6.QtCore import QTimer, QThread, Signal, Slot, Qt, QSize

class Loading():
    def __init__(self):
        
        self.loading_animation = None
        self.loading_function = None
        self.loading_dialog = LoadingDialog("assets\walking_robot.gif", "Loading...")
        self.worker = WorkerThread(self.loading_function)
    
    def set_loading_function(self, function):
        self.loading_function = function

    def run(self):
        self.worker.run()


class WorkerThread(QThread):
    finished = Signal(bool, name='new_data')  # Señal para cerrar el diálogo cuando termine
    
    def __init__(self, function):
        super().__init__()
        self.function = function

    def run(self):
        self.function()
        self.finished.emit()  # Notifica que la tarea terminó

class Dialog(QDialog):
    def __init__(self, text):
        super().__init__()

        self.text = text

        self.setWindowModality(Qt.WindowModality.ApplicationModal)  # Bloquea la ventana principal
        self.setFixedSize(100, 100)

        # Eliminar barra de título y botones de cerrar, minimizar y maximizar
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        layout = QVBoxLayout(self)
        self.label = QLabel(self.text, self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.label)
    
    def set_text(self, text):
        self.label.setText(text)

class LoadingDialog(QDialog):
    def __init__(self, gif_route, text):
        super().__init__()
        self.setWindowTitle("Cargando...")
        self.setWindowModality(Qt.WindowModality.ApplicationModal)  # Bloquea la ventana principal
        self.setFixedSize(150, 150)

        # Eliminar barra de título y botones de cerrar, minimizar y maximizar
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        layout = QVBoxLayout(self)
        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Agregar GIF animado
        self.loading_gif = QLabel(self)
        self.movie = QMovie(gif_route)  # Reemplázalo con la ruta de tu GIF de carga
        self.movie.setScaledSize(QSize(100, 100))
        self.loading_gif.setMovie(self.movie)
        self.movie.start()  # Iniciar la animación

        layout.addWidget(self.loading_gif)
        layout.addWidget(self.label)
