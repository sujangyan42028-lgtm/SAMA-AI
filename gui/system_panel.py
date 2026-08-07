from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QProgressBar
)
from PySide6.QtCore import Qt


class SystemPanel(QFrame):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(260)

        layout = QVBoxLayout(self)

        title = QLabel("SYSTEM")
        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
        color:#00ffff;
        font-size:24px;
        font-weight:bold;
        """)

        layout.addWidget(title)
        layout.addSpacing(20)

        self.cpu = self.make_bar(layout, "CPU")
        self.ram = self.make_bar(layout, "RAM")
        self.gpu = self.make_bar(layout, "GPU")
        self.network = self.make_bar(layout, "NETWORK")
        self.battery = self.make_bar(layout, "BATTERY")

        layout.addStretch()

    def make_bar(self, layout, text):

        label = QLabel(text)

        label.setStyleSheet("""
        color:white;
        font-size:14px;
        """)

        bar = QProgressBar()

        bar.setValue(0)

        layout.addWidget(label)
        layout.addWidget(bar)

        return bar

    def update_stats(
        self,
        cpu,
        ram,
        gpu,
        network,
        battery
    ):

        self.cpu.setValue(cpu)
        self.ram.setValue(ram)
        self.gpu.setValue(gpu)
        self.network.setValue(network)
        self.battery.setValue(battery)