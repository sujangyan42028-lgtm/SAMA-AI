from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QHBoxLayout
)

from PySide6.QtCore import (
    Qt,
    QTimer,
    QDateTime
)


class TopBar(QFrame):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(70)

        layout = QHBoxLayout(self)

        self.logo = QLabel("🤖 SAMA AI")

        self.logo.setStyleSheet("""
        color:#ff00ff;
        font-size:28px;
        font-weight:bold;
        """)

        layout.addWidget(self.logo)

        layout.addStretch()

        self.status = QLabel("🟢 READY")

        self.status.setStyleSheet("""
        color:#00ff99;
        font-size:16px;
        font-weight:bold;
        """)

        layout.addWidget(self.status)

        layout.addSpacing(30)

        self.clock = QLabel()

        self.clock.setStyleSheet("""
        color:#00ffff;
        font-size:18px;
        font-weight:bold;
        """)

        layout.addWidget(self.clock)

        timer = QTimer(self)
        timer.timeout.connect(self.update_clock)
        timer.start(1000)

        self.update_clock()

    def update_clock(self):

        now = QDateTime.currentDateTime()

        self.clock.setText(
            now.toString("dd MMM yyyy   hh:mm:ss AP")
        )

    def set_status(self, text):

        self.status.setText(text)