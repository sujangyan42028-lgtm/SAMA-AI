from PySide6.QtWidgets import QWidget
from PySide6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QBrush
)
from PySide6.QtCore import (
    Qt,
    QTimer
)


class AnimatedCore(QWidget):

    def __init__(self):
        super().__init__()

        self.angle = 0

        self.scale = 0

        self.direction = 1

        self.mode = "ready"

        self.timer = QTimer(self)

        self.timer.timeout.connect(self.animate)

        self.timer.start(16)

    def set_mode(self, mode):

        self.mode = mode

    def animate(self):

        self.angle += 2

        self.scale += self.direction

        if self.scale > 10:
            self.direction = -1

        if self.scale < 0:
            self.direction = 1

        self.update()

    def paintEvent(self, e):

        p = QPainter(self)

        p.setRenderHint(QPainter.Antialiasing)

        w = self.width()

        h = self.height()

        cx = w / 2

        cy = h / 2

        p.translate(cx, cy)

        # -------- COLOR -------- #

        color = QColor("#00ffff")

        if self.mode == "listening":
            color = QColor("#00ffff")

        elif self.mode == "thinking":
            color = QColor("#ff00ff")

        elif self.mode == "speaking":
            color = QColor("#00ff66")

        elif self.mode == "sleep":
            color = QColor("#666666")

        # -------- OUTER GLOW -------- #

        p.setPen(Qt.NoPen)

        p.setBrush(QBrush(QColor(
            color.red(),
            color.green(),
            color.blue(),
            25
        )))

        glow = 180 + self.scale

        p.drawEllipse(
            -glow,
            -glow,
            glow * 2,
            glow * 2
        )

        # -------- RING 1 -------- #

        p.save()

        p.rotate(self.angle)

        pen = QPen(color)

        pen.setWidth(5)

        p.setPen(pen)

        p.setBrush(Qt.NoBrush)

        p.drawArc(
            -120,
            -120,
            240,
            240,
            0 * 16,
            80 * 16
        )

        p.drawArc(
            -120,
            -120,
            240,
            240,
            120 * 16,
            80 * 16
        )

        p.drawArc(
            -120,
            -120,
            240,
            240,
            240 * 16,
            80 * 16
        )

        p.restore()

        # -------- RING 2 -------- #

        p.save()

        p.rotate(-self.angle * 1.5)

        pen = QPen(color)

        pen.setWidth(3)

        p.setPen(pen)

        p.drawArc(
            -90,
            -90,
            180,
            180,
            30 * 16,
            120 * 16
        )

        p.drawArc(
            -90,
            -90,
            180,
            180,
            210 * 16,
            120 * 16
        )

        p.restore()

        # -------- CENTER -------- #

        p.setPen(Qt.NoPen)

        p.setBrush(QBrush(color))

        radius = 22 + self.scale // 2

        p.drawEllipse(
            -radius,
            -radius,
            radius * 2,
            radius * 2
        )