import re
import sys
import time

from PySide6.QtCore import *
# from PySide6.QtGui import *
# from PySide6.QtWidgets import *
from PySide6.QtGui import QAction
from PySide2 import QtWidgets
from PySide6.QtWidgets import QGraphicsView
from PySide2.QtWidgets import QMainWindow, QGraphicsScene, QTableWidgetItem
from conf.mainwindow import Ui_MainWindow
from PySide6.QtUiTools import QUiLoader
import pyqtgraph as pg
import numpy as np
from pyqtgraph import PlotWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.menu.triggered.connect(self.action_menu)
        self.menu_2.triggered.connect(self.action_menu2)
        self.tableWidget.cellChanged.connect(self.table_widget)

    @staticmethod
    def action_menu(state):
        """
            text = "参数设置"
            toolTip = "setting"
            checked = true
            menuRole = TextHeuristicRole
            enabled = true
            visible = true
        """
        print(state.toolTip())

    @staticmethod
    def action_menu2(state):
        print(state.toolTip())

    def table_widget(self, x, y):
        print(f"Table 1 ({x},{y}) = {self.tableWidget.item(x, y).text()}")



class WidgetGraph:


    def __init__(self, widget_main):
        self.figure = plt.gcf()

        # img = plt.imread("src.jpg")  # 读取图片
        # plt.grid()  # 生成网格
        self.dynamic_canvas = FigureCanvas(self.figure)
        widget_main.verticalLayout.addWidget(NavigationToolbar(self.dynamic_canvas, widget_main))  # 添加
        widget_main.verticalLayout.addWidget(self.dynamic_canvas)

        self.dynamic_canvas.mpl_connect("button_release_event", self._on_left_click)  # 连接信号
        self.dynamic_canvas.mpl_connect('scroll_event', self._on_wheel)

        self._dynamic_ax = self.dynamic_canvas.figure.subplots()

        # self._dynamic_ax.imshow(img, extent=[0, 20, 0, 20])  # 设置图片大小

        t = np.linspace(0, 10, 101)
        # Set up a Line2D.
        self._line, = self._dynamic_ax.plot(t, np.sin(t + time.time()))
        self._timer = self.dynamic_canvas.new_timer(50)
        self._timer.add_callback(self._update_canvas)
        self._timer.start()

    def _update_canvas(self):
        t = np.linspace(0, 10, 101)
        # Shift the sinusoid as a function of time.
        self._line.set_data(t, np.sin(t + time.time()))
        self._line.figure.canvas.draw()

    def _on_left_click(self, event):
        print(event.button)
        pass

    def _on_wheel(self, event):
        print(event.button)
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    WidgetGraph(window)
    window.show()
    sys.exit(app.exec_())
