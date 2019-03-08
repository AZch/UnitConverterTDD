# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWnd.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MakeConv = QtWidgets.QPushButton(self.centralwidget)
        self.MakeConv.setGeometry(QtCore.QRect(290, 70, 121, 31))
        self.MakeConv.setObjectName("MakeConv")
        self.SIConvFrom = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.SIConvFrom.setGeometry(QtCore.QRect(10, 40, 121, 26))
        self.SIConvFrom.setDecimals(323)
        self.SIConvFrom.setMaximum(1e+23)
        self.SIConvFrom.setObjectName("SIConvFrom")
        self.cmbAllQuantFrom = QtWidgets.QComboBox(self.centralwidget)
        self.cmbAllQuantFrom.setGeometry(QtCore.QRect(10, 10, 121, 25))
        self.cmbAllQuantFrom.setObjectName("cmbAllQuantFrom")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 100, 81, 17))
        self.label.setObjectName("label")
        self.addQuant = QtWidgets.QPushButton(self.centralwidget)
        self.addQuant.setGeometry(QtCore.QRect(160, 210, 251, 31))
        self.addQuant.setObjectName("addQuant")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 120, 81, 17))
        self.label_11.setObjectName("label_11")
        self.nameQuant = QtWidgets.QLineEdit(self.centralwidget)
        self.nameQuant.setGeometry(QtCore.QRect(30, 140, 121, 21))
        self.nameQuant.setObjectName("nameQuant")
        self.cmbAllQuantTo = QtWidgets.QComboBox(self.centralwidget)
        self.cmbAllQuantTo.setGeometry(QtCore.QRect(290, 10, 121, 25))
        self.cmbAllQuantTo.setObjectName("cmbAllQuantTo")
        self.SIConvTo = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.SIConvTo.setGeometry(QtCore.QRect(290, 40, 121, 26))
        self.SIConvTo.setDecimals(323)
        self.SIConvTo.setMaximum(1e+25)
        self.SIConvTo.setObjectName("SIConvTo")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(140, 40, 141, 17))
        self.label_15.setObjectName("label_15")
        self.cmbAllQuantFrom_2 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbAllQuantFrom_2.setGeometry(QtCore.QRect(30, 180, 121, 25))
        self.cmbAllQuantFrom_2.setObjectName("cmbAllQuantFrom_2")
        self.SIConvFrom_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.SIConvFrom_2.setGeometry(QtCore.QRect(160, 180, 121, 26))
        self.SIConvFrom_2.setDecimals(323)
        self.SIConvFrom_2.setMaximum(1e+26)
        self.SIConvFrom_2.setObjectName("SIConvFrom_2")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 160, 81, 17))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(160, 160, 81, 17))
        self.label_13.setObjectName("label_13")
        self.addQuant_2 = QtWidgets.QPushButton(self.centralwidget)
        self.addQuant_2.setGeometry(QtCore.QRect(290, 180, 121, 25))
        self.addQuant_2.setObjectName("addQuant_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MakeConv.setText(_translate("MainWindow", "Конвертировать"))
        self.label.setText(_translate("MainWindow", "Добавить"))
        self.addQuant.setText(_translate("MainWindow", "Добавить величину"))
        self.label_11.setText(_translate("MainWindow", "Название"))
        self.label_15.setText(_translate("MainWindow", ">>>>>>>>>>>>>>>>"))
        self.label_12.setText(_translate("MainWindow", "Величина"))
        self.label_13.setText(_translate("MainWindow", "Значение"))
        self.addQuant_2.setText(_translate("MainWindow", "Принять"))


