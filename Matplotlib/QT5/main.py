# #-*-coding:utf-8-*-
# import re
# import sys
#
# import Matplotlib
# # from PyQt5.QtWidgets import *
# #
# # Matplotlib.use("Qt5Agg")  # 声明使用QT5
# # from Matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# # from Matplotlib.figure import Figure
# #
# # from PyQt5 import QtCore, QtWidgets
#
# class Ui_Dialog(object):
#     def setupUi(self, Dialog):
#         Dialog.setObjectName("Dialog")
#         Dialog.resize(718, 515)
#         self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
#         self.buttonBox.setGeometry(QtCore.QRect(370, 470, 341, 32))
#         self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
#         self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
#         self.buttonBox.setObjectName("buttonBox")
#         self.widget = QtWidgets.QWidget(Dialog)
#         self.widget.setGeometry(QtCore.QRect(10, 10, 691, 451))
#         self.widget.setObjectName("widget")
#         self.groupBox = QtWidgets.QGroupBox(self.widget)
#         self.groupBox.setGeometry(QtCore.QRect(0, 0, 691, 451))
#         self.groupBox.setObjectName("groupBox")
#
#         self.retranslateUi(Dialog)
#         self.buttonBox.accepted.connect(Dialog.accept)
#         self.buttonBox.rejected.connect(Dialog.reject)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#
#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
#         self.groupBox.setTitle(_translate("Dialog", " "))
#
#
# #创建一个matplotlib图形绘制类
# class MyFigure(FigureCanvas):
#     def __init__(self,width=5, height=4, dpi=100):
#         #第一步：创建一个创建Figure
#         self.fig = Figure(figsize=(width, height), dpi=dpi)
#         #第二步：在父类中激活Figure窗口
#         super(MyFigure,self).__init__(self.fig) #此句必不可少，否则不能显示图形
#         #第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
#         self.axes = self.fig.add_subplot(111)
#
#
# class MainDialogImgBW(QDialog,Ui_Dialog):
#     def __init__(self):
#         super(MainDialogImgBW,self).__init__()
#         self.setupUi(self)
#         self.setWindowTitle("显示2D图形")
#         self.setMinimumSize(0,0)
#
#         #第五步：定义MyFigure类的一个实例
#         self.F = MyFigure(width=3, height=2, dpi=100)
#         #self.F.plotsin()
#         self.plotcos()
#         #第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
#         self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox
#         self.gridlayout.addWidget(self.F,0,1)
#
#
#
#     def plotcos(self):
#         with open('20200830_180146RTLS_log.txt') as fin:
#             text = fin.read();
#             regex = r':\[([\s\S]*?)\]:'
#             matches = re.findall(regex, text)
#             strsx = []
#             strsy = []
#             strsz = []
#             for match in matches:
#                 words = match.split(',')
#                 strsx.append(words[0])
#                 strsy.append(words[1])
#                 strsz.append(words[2])
#
#         x1 = list(map(float, strsx))
#         y1 = list(map(float, strsy))
#
#
#
#         # 在同一幅图片上画两条折线
#         self.F.axes.plot(x1, y1,'r')
#         self.F.fig.suptitle("Haoru")
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main = MainDialogImgBW()
#     main.show()
#     #app.installEventFilter(main)
#     sys.exit(app.exec_())