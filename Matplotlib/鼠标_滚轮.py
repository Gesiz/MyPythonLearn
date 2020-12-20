from PySide2 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

import numpy as np


class MyPaintWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.figure = plt.gcf()



        self.canvas = FigureCanvas(self.figure)
        self.canvas.mpl_connect("button_press_event", self._on_left_click)
        self.canvas.mpl_connect('scroll_event', self._on_wheel)

        self.axes = self.figure.add_subplot(111)
        x = np.arange(0, 10, 0.1)
        y = np.cos(x)
        self.axes.plot(x, y)

        layout_canvas = QtWidgets.QVBoxLayout(self)
        layout_canvas.addWidget(self.canvas)

    def _on_left_click(self, event):
        print(event)
        self.axes.scatter(event.xdata, event.ydata)
        self.figure.canvas.draw()

    def _on_wheel(self,event):
        print(event)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = MyPaintWidget()
    w.show()
    sys.exit(app.exec_())