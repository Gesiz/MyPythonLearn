#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:dell
import sys
import numpy as np
from PySide6 import QtWidgets
import pyqtgraph as pg

from mainwindow import Ui_MainWindow


class MyGraphWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):

        super(MyGraphWindow, self).__init__()
        self.setupUi(self)  # 初始化窗口

        self.p1, self.p2 = self.set_graph_ui()  # 设置绘图窗口

        self.btn.clicked.connect(self.plot_sin_cos)  # 点击按键开始绘图

    def set_graph_ui(self):

        pg.setConfigOptions(antialias=True)  # pg全局变量设置函数，antialias=True开启曲线抗锯齿

        win = pg.GraphicsLayoutWidget()  # 创建pg layout，可实现数据界面布局自动管理

        # pg绘图窗口可以作为一个widget添加到GUI中的graph_layout，当然也可以添加到Qt其他所有的容器中
        self.graph_layout.addWidget(win)

        p1 = win.addPlot(title="sin 函数")  # 添加第一个绘图窗口
        p1.setLabel('left', text='meg', color='#ffffff')  # y轴设置函数
        p1.showGrid(x=True, y=True)  # 栅格设置函数
        p1.setLogMode(x=False, y=False)  # False代表线性坐标轴，True代表对数坐标轴
        p1.setLabel('bottom', text='time', units='s')  # x轴设置函数
        # p1.addLegend()  # 可选择是否添加legend

        win.nextRow()  # layout换行，采用垂直排列，不添加此行则默认水平排列
        p2 = win.addPlot(title="cos 函数")
        p2.setLabel('left', text='meg', color='#ffffff')
        p2.showGrid(x=True, y=True)
        p2.setLogMode(x=False, y=False)
        p2.setLabel('bottom', text='time', units='s')
        # p2.addLegend()

        return p1, p2

    def plot_sin_cos(self):
        t = np.linspace(0, 20, 200)
        y_sin = np.sin(t)
        y_cos = np.cos(t)
        self.p1.plot(t, y_sin, pen='g', name='sin(x)', clear=True)
        self.p2.plot(t, y_cos, pen='g', name='con(x)', clear=True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWin = MyGraphWindow()
    myWin.show()
    sys.exit(app.exec_())