# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from graph_design import Ui_painter


class Draw_graph(QMainWindow, Ui_painter):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
ex = Draw_graph()


def running():
    try:
        left, rigth = int(ex.left.text()), int(ex.right.text())
    except:
        left, rigth = -1000, 1000

    try:
        a, b, c = int(ex.A.text()), int(ex.B.text()), int(ex.C.text())
    except:
        a, b, c = 1, 1, 1

    ex.graphic.clear()
    ex.graphic.plot([i for i in range(left, rigth + 1)], [(a * j * j + b * j + c) for j in range(left, rigth + 1)],
                         pen='r')


ex.draw.clicked.connect(running)
ex.show()
sys.exit(app.exec_())
