import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QBrush, QPen, QPainter, QPolygon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot, QPoint, Qt
from math import cos, sin, radians


class HexPushButton(QPushButton):
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        line_width = 3
        painter.setPen(QPen(Qt.black, line_width, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))

        gap = 6
        side_length = (min(self.size().width(), self.size().height()) / 2) - 2 * gap - 2 * line_width
        location = [side_length + gap + line_width] * 2
        tri_angle = 30
        hex_angle = 0

        for i in range(0, 6, 1):
            location[0] += gap * cos(radians(hex_angle))
            location[1] += gap * sin(radians(hex_angle))
            points = []

            for j in range(0, 3, 1):
                points.append(QPoint(location[0], location[1]))
                location[0] += side_length * cos(radians(tri_angle))
                location[1] += side_length * sin(radians(tri_angle))
                tri_angle -= 120

            points = QPolygon(points)
            painter.drawPolygon(points)

            location[0] -= gap * cos(radians(hex_angle))
            location[1] -= gap * sin(radians(hex_angle))
            hex_angle += 60
            tri_angle += 60


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'autoHive'
        self.left = 50
        self.top = 50
        self.width = 320
        self.height = 200
        self.demoUI()

    def demoUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        hexagon = HexPushButton('', self)
        hexagon.setToolTip('Joint')
        hexagon.setGeometry(100, 40, 120, 120)
        hexagon.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('Clicked')


def gui():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
