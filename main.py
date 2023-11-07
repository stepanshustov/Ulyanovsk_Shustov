import random
import sys
import io

from PyQt5.QtGui import QPainter, QColor, QPixmap, QImage, QTransform
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFileDialog, QLabel, QMainWindow
from PyQt5.QtCore import QPoint
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print(1)
        uic.loadUi("UI.ui", self)
        self.flag = 0
        self.pushButton.clicked.connect(self.draw_yellow_cicle)

    def draw_yellow_cicle(self):
        self.flag = 1
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.flag = 0
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            x, y = random.randint(80, self.x()), random.randint(60, self.y())
            d = random.randint(10, min(self.x(), self.y()) - 50)
            qp.drawEllipse(x, y, d, d)
            qp.end()
        self.flag = 0





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
