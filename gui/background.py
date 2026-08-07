from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import QTimer
import random


class Background(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.points = []

        for _ in range(80):
            self.points.append([
                random.randint(0, 1600),
                random.randint(0, 900),
                random.randint(-2, 2),
                random.randint(-2, 2)
            ])

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(30)

    def animate(self):

        w = max(1, self.width())
        h = max(1, self.height())

        for p in self.points:

            p[0] += p[2]
            p[1] += p[3]

            if p[0] < 0 or p[0] > w:
                p[2] *= -1

            if p[1] < 0 or p[1] > h:
                p[3] *= -1

        self.update()

    def paintEvent(self, e):

        painter = QPainter(self)

        painter.fillRect(self.rect(), QColor(10, 10, 20))

        painter.setPen(QColor(0, 255, 255, 120))

        for p in self.points:

            painter.drawEllipse(p[0], p[1], 3, 3)

        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):

                x1, y1 = self.points[i][:2]
                x2, y2 = self.points[j][:2]

                if (x1 - x2) ** 2 + (y1 - y2) ** 2 < 120 ** 2:
                    painter.drawLine(x1, y1, x2, y2)