# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design2_fortepiano.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_player(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Do = QtWidgets.QPushButton(self.centralwidget)
        self.Do.setGeometry(QtCore.QRect(70, 90, 93, 28))
        self.Do.setObjectName("Do")
        self.Re = QtWidgets.QPushButton(self.centralwidget)
        self.Re.setGeometry(QtCore.QRect(70, 130, 93, 28))
        self.Re.setObjectName("Re")
        self.Mi = QtWidgets.QPushButton(self.centralwidget)
        self.Mi.setGeometry(QtCore.QRect(70, 170, 93, 28))
        self.Mi.setObjectName("Mi")
        self.Fa = QtWidgets.QPushButton(self.centralwidget)
        self.Fa.setGeometry(QtCore.QRect(70, 210, 93, 28))
        self.Fa.setObjectName("Fa")
        self.Sol = QtWidgets.QPushButton(self.centralwidget)
        self.Sol.setGeometry(QtCore.QRect(70, 250, 93, 28))
        self.Sol.setObjectName("Sol")
        self.La = QtWidgets.QPushButton(self.centralwidget)
        self.La.setGeometry(QtCore.QRect(70, 290, 93, 28))
        self.La.setObjectName("La")
        self.Si = QtWidgets.QPushButton(self.centralwidget)
        self.Si.setGeometry(QtCore.QRect(70, 330, 93, 28))
        self.Si.setObjectName("Si")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.Do.setText(_translate("MainWindow", "До"))
        self.Re.setText(_translate("MainWindow", "Ре"))
        self.Mi.setText(_translate("MainWindow", "Ми"))
        self.Fa.setText(_translate("MainWindow", "Фа"))
        self.Sol.setText(_translate("MainWindow", "Соль"))
        self.La.setText(_translate("MainWindow", "Ля"))
        self.Si.setText(_translate("MainWindow", "Си"))
