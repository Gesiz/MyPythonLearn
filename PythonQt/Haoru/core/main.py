import re
import sys
import time

import cv2

import serial.tools.list_ports
from PySide6.QtCore import *
# from PySide6.QtGui import *
# from PySide6.QtWidgets import *
from PySide6.QtGui import QAction
from PySide2 import QtWidgets
from PySide6.QtWidgets import QGraphicsView
from PySide2.QtWidgets import QMainWindow, QGraphicsScene, QTableWidgetItem
from matplotlib.ticker import MultipleLocator

from conf.mainwindow import Ui_MainWindow
from PySide6.QtUiTools import QUiLoader
import pyqtgraph as pg
import numpy as np
from pyqtgraph import PlotWidget
from PIL import Image
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import matplotlib.pyplot as plt

import matplotlib

# matplotlib.rcParams['figure.figsize'] = [10, 10] # for square canvas
matplotlib.rcParams['figure.subplot.left'] = 0.06
matplotlib.rcParams['figure.subplot.bottom'] = 0.06
matplotlib.rcParams['figure.subplot.right'] = 0.99
matplotlib.rcParams['figure.subplot.top'] = 1


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.menu.triggered.connect(self.action_menu)
        self.menu_2.triggered.connect(self.action_menu2)
        self.tableWidget.cellChanged.connect(self.table_widget)

        self.pushButton.clicked.connect(self.connect_ser)
        self.pushButton_2.clicked.connect(self.setOpenFileName)
        self.pushButton_3.clicked.connect(self.search_ser)

        frameStyle = QtWidgets.QFrame.Sunken | QtWidgets.QFrame.Panel
        self.openFileNameLabel = QtWidgets.QLabel()
        self.openFileNameLabel.setFrameStyle(frameStyle)

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

    def setOpenFileName(self):
        options = QtWidgets.QFileDialog.Options()
        if not self.pushButton_2.isChecked():
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, filtr = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                "打开文件",
                                                                self.openFileNameLabel.text(),
                                                                "png Files (*.png);;jpg Files (*.jpg)", "", options)

        if fileName:
            self.verticalLayout_4.removeWidget(self.widget)
            WidgetGraph(window)
            print(fileName)

    def search_ser(self):

        self.comboBox.clear()
        port_list = list(serial.tools.list_ports.comports())
        for i in port_list:
            self.comboBox.addItem(i.device)

    def connect_ser(self):
        print(self.comboBox.currentIndex(), self.comboBox.currentText())


class WidgetGraph:

    def __init__(self, widget_main):
        self.fig, self.ax = plt.subplots()

        image = Image.open("C:/Users/Gei/Desktop/MyPythonLearn/PythonQt/Haoru/core/src.png")
        w, h = image.size
        scale = 1.0 * w / 2000
        new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)

        img = plt.imread("src.png")

        # self.ax.set_xlim(0, 280)  # 初始函数，设置绘图范围
        # self.ax.set_ylim(0, 150)

        # # 修改主刻度
        # xmajorLocator = MultipleLocator(100)  # 将x主刻度标签设置为20的倍数
        #
        # ymajorLocator = MultipleLocator(100)  # 将y轴主刻度标签设置为0.5的倍数
        #
        # self.ax.xaxis.set_major_locator(xmajorLocator)
        #
        # self.ax.yaxis.set_major_locator(ymajorLocator)
        # xminorLocator = MultipleLocator(20)  # 将x轴次刻度标签设置为5的倍数
        # yminorLocator = MultipleLocator(20)  # 将此y轴次刻度标签设置为0.1的倍数
        # self.ax.xaxis.set_minor_locator(xminorLocator)
        # self.ax.yaxis.set_minor_locator(yminorLocator)
        # plt.figure(figsize=(img.shape[1], img.shape[0]), dpi=100)
        # my_x_ticks = np.arange(0, 280, 10)
        # my_y_ticks = np.arange(0, 150, 10)
        # plt.xticks(my_x_ticks)
        # plt.yticks(my_y_ticks)

        imgx = img.shape[1]
        imgy = img.shape[0]

        # imgx = imgx / 10
        #
        # imgy = imgy / 10

        self.ax.imshow(new_im, extent=[0, 280, 0, 150])  # 设置图片大小

        plt.grid()

        self.dynamic_canvas = FigureCanvas(self.fig)

        widget_main.verticalLayout_4.addWidget(NavigationToolbar(self.dynamic_canvas, widget_main))  # 添加
        widget_main.verticalLayout_4.addWidget(self.dynamic_canvas)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # WidgetGraph(window)
    window.show()
    sys.exit(app.exec_())
