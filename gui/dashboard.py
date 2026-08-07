from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from gui.topbar import TopBar
from gui.system_panel import SystemPanel
from gui.chat_panel import ChatPanel
from gui.animated_core import AnimatedCore


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        root = QVBoxLayout(self)

        self.top = TopBar()

        root.addWidget(self.top)

        body = QHBoxLayout()

        self.system = SystemPanel()
        self.core = AnimatedCore()
        self.chat = ChatPanel()

        body.addWidget(self.system)
        body.addWidget(self.core, 1)
        body.addWidget(self.chat)

        root.addLayout(body)