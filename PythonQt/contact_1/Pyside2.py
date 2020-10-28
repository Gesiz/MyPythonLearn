# lesson 1
# from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
#
#
# class Stats():
#     def __init__(self):
#         self.window = QMainWindow()
#         self.window.resize(500, 400)
#         self.window.move(300, 300)
#         self.window.setWindowTitle('薪资统计')
#
#         self.textEdit = QPlainTextEdit(self.window)
#         self.textEdit.setPlaceholderText("请输入薪资表")
#         self.textEdit.move(10, 25)
#         self.textEdit.resize(300, 350)
#
#         self.button = QPushButton('统计', self.window)
#         self.button.move(380, 80)
#
#         self.button.clicked.connect(self.handleCalc)
#
#     def handleCalc(self):
#         info = self.textEdit.toPlainText()
#
#         # 薪资20000 以上 和 以下 的人员名单
#         salary_above_20k = ''
#         salary_below_20k = ''
#         for line in info.splitlines():
#             if not line.strip():
#                 continue
#             parts = line.split(' ')
#             # 去掉列表中的空字符串内容
#             parts = [p for p in parts if p]
#             name, salary, age = parts
#             if int(salary) >= 20000:
#                 salary_above_20k += name + '\n'
#             else:
#                 salary_below_20k += name + '\n'
#
#         QMessageBox.about(self.window,
#                           '统计结果',
#                           f'''薪资20000 以上的有：\n{salary_above_20k}
#                     \n薪资20000 以下的有：\n{salary_below_20k}'''
#                           )
#
#
# app = QApplication([])
# stats = Stats()
# stats.window.show()
# app.exec_()

# lesson2

# from PySide2.QtWidgets import QApplication, QMessageBox
# from PySide2.QtUiTools import QUiLoader
# from PySide2.QtCore import QFile
#
# class Stats:
#
#     def __init__(self):
#         # 从文件中加载UI定义
#         qfile_stats = QFile("ui/stats.ui")
#         qfile_stats.open(QFile.ReadOnly)
#         qfile_stats.close()
#         # 从 UI 定义中动态 创建一个相应的窗口对象
#         # 注意：里面的控件对象也成为窗口对象的属性了
#         # 比如 self.ui.button , self.ui.textEdit
#         self.ui = QUiLoader().load(qfile_stats)
#
#         self.ui.button.clicked.connect(self.handleCalc)
#
#     def handleCalc(self):
#         info = self.ui.textEdit.toPlainText()
#
#         salary_above_20k = ''
#         salary_below_20k = ''
#         for line in info.splitlines():
#             if not line.strip():
#                 continue
#             parts = line.split(' ')
#
#             parts = [p for p in parts if p]
#             name,salary,age = parts
#             if int(salary) >= 20000:
#                 salary_above_20k += name + '\n'
#             else:
#                 salary_below_20k += name + '\n'
#
#         QMessageBox.about(self.ui,
#                     '统计结果',
#                     f'''薪资20000 以上的有：\n{salary_above_20k}
#                     \n薪资20000 以下的有：\n{salary_below_20k}'''
#                     )
#
#
# app = QApplication([])
# stats = Stats()
# stats.ui.show()
# app.exec_()

# lesson 3
# from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit
#
# app = QApplication([])
#
# window = QMainWindow()
# window.resize(500, 400)
# window.move(300, 310)
# window.setWindowTitle('薪资统计')
#
# textEdit = QPlainTextEdit(window)
# textEdit.setPlaceholderText("请输入薪资表")
# textEdit.move(10,25)
# textEdit.resize(300,350)
#
# button = QPushButton('统计', window)
# button.move(380,80)
#
# window.show()
#
# app.exec_()

# !/usr/bin/env python3
import sys
import time
import re
import numpy as np
import matplotlib.pyplot as plt
from PySide2 import QtCore, QtWidgets

if QtCore.qVersion() >= "5.":
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

from matplotlib.figure import Figure


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(static_canvas)
        self.addToolBar(NavigationToolbar(static_canvas, self))

        with open('20200830_180146RTLS_log.txt') as fin:
            text = fin.read();
            regex = r':\[([\s\S]*?)\]:'
            matches = re.findall(regex, text)
            strsx = []
            strsy = []
            strsz = []
            for match in matches:
                words = match.split(',')
                strsx.append(words[0])
                strsy.append(words[1])
                strsz.append(words[2])

        x1 = list(map(float, strsx))
        y1 = list(map(float, strsy))

        self._static_ax = static_canvas.figure.subplots()

        self._static_ax.plot(x1, y1, '-r', label='A', linewidth=5.0)


if __name__ == "__main__":
    # Check whether there is already a running QApplication (e.g., if running
    # from an IDE).
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    app = ApplicationWindow()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec_()
