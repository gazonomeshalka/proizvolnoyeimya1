from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter
from random import randint
from PyQt5 import QtCore


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ГШ.ui', self)
        self.btn.clicked.connect(self.update)
        self.r = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setBrush(QtCore.Qt.yellow)
        painter.drawEllipse(300 - (self.r // 2), 300 - (self.r // 2), self.r, self.r)

    def update(self):
        self.r = randint(1, 500)
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
