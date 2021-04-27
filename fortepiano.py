# -*- coding: utf-8 -*-
import sys
from play import Ui_player
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtMultimedia


class MyWidget(QMainWindow, Ui_player):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_mp3('music/1.mp3')
        self.Do.clicked.connect(self.player.play)
        self.load_mp3('music/2.mp3')
        self.Re.clicked.connect(self.player.play)
        self.load_mp3('music/3.mp3')
        self.Mi.clicked.connect(self.player.play)
        self.load_mp3('music/4.mp3')
        self.Fa.clicked.connect(self.player.play)
        self.load_mp3('music/5.mp3')
        self.Sol.clicked.connect(self.player.play)
        self.load_mp3('music/6.mp3')
        self.La.clicked.connect(self.player.play)
        self.load_mp3('music/7.mp3')
        self.Si.clicked.connect(self.player.play)

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())