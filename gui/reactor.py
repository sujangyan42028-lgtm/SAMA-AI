from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt, QTimer
import math


class Reactor(QWidget):

    def __init__(self):
        super().__init__()

        self.radius = 80
        self.grow = True
        self.core_size = 30
        self.core_grow = True
        self.state = "ready"

        self.angle = 0
        self.orbit = 0
        self.particles = []

        import random

        for _ in range(35):

            self.particles.append({

                "angle": random.randint(0, 360),
                "radius": random.randint(110, 170),
                "speed": random.uniform(0.5, 2.5),
                "size": random.randint(2, 5)

            })
        self.glow = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(30)

    def set_state(self, state):

        self.state = state

        if state == "listening":
            self.radius = 95

        elif state == "thinking":
            self.radius = 85

        elif state == "speaking":
            self.radius = 100

        elif state == "sleep":
            self.radius = 75

        else:
            self.radius = 80

        self.update()

    def animate(self):

        self.angle += 2
        self.orbit += 5

        if self.orbit >= 360:
            self.orbit = 0
        # Core pulse animation

        if self.core_grow:
            self.core_size += 0.4
            if self.core_size >= 38:
                self.core_grow = False
        else:
            self.core_size -= 0.4
            if self.core_size <= 30:
                self.core_grow = True
        if self.state == "sleep":
            self.update()
            return

        if self.grow:
            self.radius += 1
            if self.radius >= 95:
                self.grow = False
        else:
            self.radius -= 1
            if self.radius <= 80:
                self.grow = True

        self.update()
        for particle in self.particles:

            particle["angle"] += particle["speed"]

            if particle["angle"] > 360:
                particle["angle"] = 0
    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        cx = self.width() / 2
        cy = self.height() / 2

        # Select color by state
        color = QColor("#00FFFF")

        if self.state == "thinking":
            color = QColor("#FF00FF")

        elif self.state == "speaking":
            color = QColor("#00FF66")

        elif self.state == "sleep":
            color = QColor("#555555")
        # ==========================
        # Floating Particles
        # ==========================

        painter.setPen(Qt.NoPen)

        for particle in self.particles:

            a = math.radians(particle["angle"])

            x = cx + math.cos(a) * particle["radius"]
            y = cy + math.sin(a) * particle["radius"]

            c = QColor(color)
            c.setAlpha(120)

            painter.setBrush(c)

            painter.drawEllipse(
                int(x),
                int(y),
                particle["size"],
                particle["size"]
            )

        # ==========================
        # Radar Scan Ring
        # ==========================

        scan_radius = self.radius + 90

        scan_pen = QPen(QColor(0, 255, 255, 180))
        scan_pen.setWidth(2)

        painter.setPen(scan_pen)
        painter.setBrush(Qt.NoBrush)

        start = self.angle * 16
        span = 20 * 16

        painter.drawArc(
            int(cx - scan_radius),
            int(cy - scan_radius),
            scan_radius * 2,
            scan_radius * 2,
            start,
            span
        )
        # ==========================
        # Electric Energy Arcs
        # ==========================

        arc_pen = QPen(color)
        arc_pen.setWidth(3)

        arc_color = QColor(color)
        arc_color.setAlpha(180)

        arc_pen.setColor(arc_color)

        painter.setPen(arc_pen)
        painter.setBrush(Qt.NoBrush)

        for i in range(3):

            start = (self.angle * 16) + (i * 120 * 16)

            span = 35 * 16

            painter.drawArc(
                int(cx - (self.radius + 8)),
                int(cy - (self.radius + 8)),
                (self.radius + 8) * 2,
                (self.radius + 8) * 2,
                start,
                span
    )
        # Orbiting Energy Particle

        particle_angle = math.radians(self.orbit)

        particle_radius = self.radius + 15

        px = cx + math.cos(particle_angle) * particle_radius
        py = cy + math.sin(particle_angle) * particle_radius

        glow = QColor(color)
        glow.setAlpha(80)

        painter.setBrush(glow)
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(
            int(px - 8),
            int(py - 8),
            16,
            16
        )

        painter.setBrush(color)

        painter.drawEllipse(
            int(px - 4),
            int(py - 4),
            8,
            8
        )
        # ==========================
        # Electric Lightning
        # ==========================

        if self.state in ["speaking", "thinking"]:

            lightning_pen = QPen(QColor(255, 255, 255, 180))
            lightning_pen.setWidth(2)

            painter.setPen(lightning_pen)

            import random

            for _ in range(4):

                angle = math.radians(random.randint(0, 360))

                x1 = cx + math.cos(angle) * (self.radius - 10)
                y1 = cy + math.sin(angle) * (self.radius - 10)

                x2 = cx + math.cos(angle) * (self.radius + 20)
                y2 = cy + math.sin(angle) * (self.radius + 20)

                painter.drawLine(
                    int(x1),
                    int(y1),
                    int(x2),
                    int(y2)
                )
        # Rotating dots
        # Outer rotating ring

        pen = QPen(color)
        pen.setWidth(2)

        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)

        outer_radius = self.radius + 50
        middle_radius = self.radius + 65
        inner_radius = self.radius + 20
        start_angle = self.angle * 16

        span_angle = 90 * 16

        painter.drawArc(
            int(cx - outer_radius),
            int(cy - outer_radius),
            outer_radius * 2,
            outer_radius * 2,
            start_angle,
            span_angle
        )
        # Second Ring

        painter.drawArc(
            int(cx - middle_radius),
            int(cy - middle_radius),
            middle_radius * 2,
            middle_radius * 2,
            -(start_angle * 2),
            60 * 16
        )

        # Third Ring

        painter.drawArc(
            int(cx - inner_radius),
            int(cy - inner_radius),
            inner_radius * 2,
            inner_radius * 2,
            start_angle * 3,
            45 * 16
        )
        painter.drawArc(
            int(cx - outer_radius),
            int(cy - outer_radius),
            outer_radius * 2,
            outer_radius * 2,
            (start_angle + 180 * 16),
            span_angle
)
        painter.setPen(Qt.NoPen)
        painter.setBrush(color)

        for i in range(12):

            angle = math.radians(self.angle + i * 30)

            x = cx + math.cos(angle) * (self.radius + 35)
            y = cy + math.sin(angle) * (self.radius + 35)

            painter.drawEllipse(
                int(x - 3),
                int(y - 3),
                6,
                6
            )
        # ==========================
        # Bloom Glow
        # ==========================

        for i in range(10):

            glow = QColor(color)
            glow.setAlpha(max(5, 35 - i * 3))

            glow_pen = QPen(glow)
            glow_pen.setWidth(18 - i)

            painter.setPen(glow_pen)
            painter.setBrush(Qt.NoBrush)

            r = self.radius + i

            painter.drawEllipse(
                int(cx - r),
                int(cy - r),
                r * 2,
                r * 2
            )
        # Outer Ring
        pen = QPen(color)
        pen.setWidth(5)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        # Glow effect
        for i in range(6):

            glow_pen = QPen(color)

            glow_pen.setWidth(12 - i * 2)

            glow_color = QColor(color)
            glow_color.setAlpha(25 - i * 4)

            glow_pen.setColor(glow_color)

            painter.setPen(glow_pen)

            painter.drawEllipse(
                int(cx - self.radius),
                int(cy - self.radius),
                self.radius * 2,
                self.radius * 2
    )
        painter.drawEllipse(
            int(cx - self.radius),
            int(cy - self.radius),
            self.radius * 2,
            self.radius * 2
        )

        # Inner Ring
        painter.drawEllipse(
            int(cx - self.radius + 25),
            int(cy - self.radius + 25),
            (self.radius - 25) * 2,
            (self.radius - 25) * 2
        )

        # Core
        painter.setPen(Qt.NoPen)
        painter.setBrush(color)

        # Animated Core

        size = int(self.core_size)

        painter.setPen(Qt.NoPen)
        painter.setBrush(color)

        painter.drawEllipse(
            int(cx - size / 2),
            int(cy - size / 2),
            size,
            size
        )
        if self.state == "speaking":

            blast_pen = QPen(QColor(0, 255, 120, 120))
            blast_pen.setWidth(4)

            painter.setPen(blast_pen)
            painter.setBrush(Qt.NoBrush)

            r = self.radius + 20

            painter.drawEllipse(
                int(cx - r),
                int(cy - r),
                r * 2,
                r * 2
            )