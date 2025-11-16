from pyqtgraph import PlotWidget
from collections import deque

# from PySide6.GraphicsView import GraphicsView


class RealTimePlotWidget(PlotWidget):
    def __init__(self, max_points=100, margin=10, plot: PlotWidget = None):
        super().__init__()

        self.max_points = max_points
        self.margin = margin

        # # Crear la curva que se actualizará con los datos
        # self.plot(pen='y')

        # Inicializar los datos (con deque para mantener solo los últimos puntos)
        self.data = deque(maxlen=self.max_points)
        self.time = deque(maxlen=self.max_points)
        self.time_counter = 0

    def update_plot(self, data):
        self.time.append(self.timer_counter)
        self.data.append(data)
        self.plot(list(self.data_x), list(self.data_y))
        self.timer_counter += 1

        print(f"Deque: {len(self.data_x)}")
        if self.timer_counter > self.ant_timer_value + 100:
            self.ant_timer_value = self.timer_counter

        self.ui.graphWidget.setXRange(
            self.timer_counter - 100, self.timer_counter)
