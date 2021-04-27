# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_painter(object):
    def setupUi(self, painter):
        painter.setObjectName("painter")
        painter.resize(806, 827)
        self.centralwidget = QtWidgets.QWidget(painter)
        self.centralwidget.setObjectName("centralwidget")
        self.C = QtWidgets.QLineEdit(self.centralwidget)
        self.C.setGeometry(QtCore.QRect(140, 630, 110, 24))
        self.C.setObjectName("C")
        self.label_C = QtWidgets.QLabel(self.centralwidget)
        self.label_C.setGeometry(QtCore.QRect(60, 630, 68, 16))
        self.label_C.setObjectName("label_C")
        self.B = QtWidgets.QLineEdit(self.centralwidget)
        self.B.setGeometry(QtCore.QRect(140, 590, 110, 24))
        self.B.setObjectName("B")
        self.draw = QtWidgets.QPushButton(self.centralwidget)
        self.draw.setEnabled(True)
        self.draw.setGeometry(QtCore.QRect(50, 680, 121, 31))
        self.draw.setToolTipDuration(-1)
        self.draw.setObjectName("draw")
        self.graphic = PlotWidget(self.centralwidget)
        self.graphic.setGeometry(QtCore.QRect(11, 11, 741, 441))
        self.graphic.setObjectName("graphic")
        self.label_B = QtWidgets.QLabel(self.centralwidget)
        self.label_B.setGeometry(QtCore.QRect(60, 590, 67, 16))
        self.label_B.setObjectName("label_B")
        self.A = QtWidgets.QLineEdit(self.centralwidget)
        self.A.setGeometry(QtCore.QRect(140, 550, 110, 24))
        self.A.setObjectName("A")
        self.label_A = QtWidgets.QLabel(self.centralwidget)
        self.label_A.setGeometry(QtCore.QRect(60, 550, 68, 16))
        self.label_A.setObjectName("label_A")
        self.lab_left = QtWidgets.QLabel(self.centralwidget)
        self.lab_left.setGeometry(QtCore.QRect(390, 580, 41, 16))
        self.lab_left.setObjectName("lab_left")
        self.left = QtWidgets.QLineEdit(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(450, 580, 110, 24))
        self.left.setObjectName("left")
        self.rigth = QtWidgets.QLineEdit(self.centralwidget)
        self.rigth.setGeometry(QtCore.QRect(450, 620, 110, 24))
        self.rigth.setObjectName("rigth")
        self.label_rigth = QtWidgets.QLabel(self.centralwidget)
        self.label_rigth.setGeometry(QtCore.QRect(390, 620, 41, 16))
        self.label_rigth.setObjectName("label_rigth")
        self.label_form = QtWidgets.QLabel(self.centralwidget)
        self.label_form.setGeometry(QtCore.QRect(70, 500, 211, 31))
        self.label_form.setObjectName("label_form")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 540, 221, 16))
        self.label_2.setObjectName("label_2")
        painter.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(painter)
        self.statusbar.setObjectName("statusbar")
        painter.setStatusBar(self.statusbar)

        self.retranslateUi(painter)
        QtCore.QMetaObject.connectSlotsByName(painter)

    def retranslateUi(self, painter):
        _translate = QtCore.QCoreApplication.translate
        painter.setWindowTitle(_translate("painter", "MainWindow"))
        self.label_C.setText(_translate("painter", "Введите C:"))
        self.draw.setText(_translate("painter", "Построить"))
        self.label_B.setText(_translate("painter", "Введите B:"))
        self.label_A.setText(_translate("painter", "Введите A:"))
        self.lab_left.setText(_translate("painter", "левая"))
        self.label_rigth.setText(_translate("painter", "правая"))
        self.label_form.setText(_translate("painter", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">y = A * x ^ 2 + B * x + C</span></p></body></html>"))
        self.label_2.setText(_translate("painter", "Задайте диапазон через границы:"))
from pyqtgraph import PlotWidget
