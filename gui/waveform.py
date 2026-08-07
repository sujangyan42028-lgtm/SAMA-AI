from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import QTimer, Qt
import random


class Waveform(QWidget):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(320, 100)

        self.values = [20] * 40
        self.active = False

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(40)

    def start(self):
        self.active = True

    def stop(self):
        self.active = False

    def animate(self):

        if self.active:
            self.values = [
                random.randint(15, 80)
                for _ in range(40)
            ]
        else:
            self.values = [15] * 40

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(self.rect(), Qt.transparent)

        w = self.width() / len(self.values)
        center = self.height() / 2

        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#00FFFF"))

        for i, h in enumerate(self.values):

            x = i * w
            y = center - h / 2

            painter.drawRoundedRect(
                int(x),
                int(y),
                int(w - 3),
                int(h),
                3,
                3
            )