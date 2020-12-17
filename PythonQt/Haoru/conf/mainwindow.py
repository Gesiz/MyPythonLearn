# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(816, 600)
        self.action123 = QAction(MainWindow)
        self.action123.setObjectName(u"action123")
        self.action123.setCheckable(True)
        self.action345 = QAction(MainWindow)
        self.action345.setObjectName(u"action345")
        self.action345.setCheckable(True)
        self.action123_2 = QAction(MainWindow)
        self.action123_2.setObjectName(u"action123_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 816, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action123)
        self.menu.addAction(self.action345)
        self.menu_2.addAction(self.action123_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action123.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.action345.setText(QCoreApplication.translate("MainWindow", u"\u7f29\u7565\u5e95\u56fe", None))
        self.action123_2.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u6d69\u5982\u79d1\u6280", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u663e\u793a", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

