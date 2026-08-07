from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QFrame,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QProgressBar,
    QStackedLayout
)
from gui.signals import signals
from PySide6.QtCore import Qt, QTimer, QTime
from gui.waveform import Waveform
from gui.system_monitor import SystemMonitor
from gui.styles import STYLE
from gui.reactor import Reactor
from gui.background import Background
from gui.waveform import Waveform

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("SAMA AI")
        self.resize(1500, 850)

        self.setStyleSheet(STYLE)

        central = QWidget()
        self.setCentralWidget(central)

        # ---------- Animated Background ----------

        bg = Background(central)
        bg.lower()

        foreground = QWidget(central)
        foreground.setAttribute(Qt.WA_TranslucentBackground)

        foreground.setGeometry(self.rect())

        # ---------- CLOCK ----------

        self.clock = QLabel()
        self.clock.setAlignment(Qt.AlignRight)

        self.clock.setStyleSheet("""
        font-size:18px;
        font-weight:bold;
        color:#00ffff;
        """)

        self.clock_timer = QTimer()
        self.clock_timer.timeout.connect(self.update_clock)
        self.clock_timer.start(1000)
        self.update_clock()

        # ---------- MAIN LAYOUT ----------

        main_layout = QVBoxLayout(foreground)

        top_bar = QHBoxLayout()

        logo = QLabel("🤖 SAMA AI")

        logo.setStyleSheet("""
        font-size:30px;
        font-weight:bold;
        color:#ff00ff;
        """)

        top_bar.addWidget(logo)
        top_bar.addStretch()
        top_bar.addWidget(self.clock)

        main_layout.addLayout(top_bar)

        root = QHBoxLayout()

        main_layout.addLayout(root)

        # ---------- LEFT ----------

        left = QFrame()
        left.setFixedWidth(250)

        left_layout = QVBoxLayout(left)

        title = QLabel("SYSTEM")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)

        self.cpu = QProgressBar()
        self.ram = QProgressBar()
        self.net = QProgressBar()

        left_layout.addWidget(title)
        left_layout.addSpacing(20)

        left_layout.addWidget(QLabel("CPU"))
        left_layout.addWidget(self.cpu)

        left_layout.addWidget(QLabel("RAM"))
        left_layout.addWidget(self.ram)

        left_layout.addWidget(QLabel("NETWORK"))
        left_layout.addWidget(self.net)

        left_layout.addStretch()

        # ---------- CENTER ----------

        center = QFrame()

        center_layout = QVBoxLayout(center)

        self.status = QLabel("🟢 READY")
        self.status.setObjectName("status")
        self.status.setAlignment(Qt.AlignCenter)

        self.core = Reactor()
        self.core.setMinimumSize(350, 350)

        self.wave = Waveform()
        self.wave.setFixedHeight(80)

        center_layout.addStretch()

        center_layout.addWidget(self.status)

        center_layout.addWidget(
            self.core,
            alignment=Qt.AlignCenter
        )

        center_layout.addWidget(
            self.wave,
            alignment=Qt.AlignCenter
        )

        center_layout.addStretch()
        self.wave = Waveform()
        self.wave.setFixedSize(320, 120)
        self.wave.setStyleSheet("background: transparent;")
        center_layout.addWidget(
            self.wave,
            alignment=Qt.AlignCenter
)
        # ---------- RIGHT ----------

        right = QFrame()
        right.setFixedWidth(400)

        right_layout = QVBoxLayout(right)

        chat_title = QLabel("💬 Conversation")

        chat_title.setStyleSheet("""
        font-size:18px;
        color:#00ffff;
        font-weight:bold;
        """)

        right_layout.addWidget(chat_title)

        self.chat = QTextEdit()
        self.chat.setObjectName("chat")
        self.chat.setReadOnly(True)

        right_layout.addWidget(self.chat)

        # ---------- ROOT ----------

        root.addWidget(left)
        root.addWidget(center, 1)
        root.addWidget(right)

        # ---------- SYSTEM ----------

        self.monitor_timer = QTimer()
        self.monitor_timer.timeout.connect(self.update_system)
        self.monitor_timer.start(1000)

        self.update_system()
        # ---------- CONNECT SIGNALS ----------

        signals.add_message.connect(self.add_message)

        signals.listening.connect(self.listening)

        signals.thinking.connect(self.thinking)

        signals.speaking.connect(self.speaking)

        signals.ready.connect(self.ready)

        signals.sleep.connect(self.sleep)
    # ---------- CLOCK ----------

    def update_clock(self):
        self.clock.setText(
            QTime.currentTime().toString("hh:mm:ss")
        )

    # ---------- SYSTEM ----------

    def update_system(self):
        self.cpu.setValue(SystemMonitor.cpu())
        self.ram.setValue(SystemMonitor.ram())
        self.net.setValue(SystemMonitor.network())

    # ---------- CHAT ----------

    def add_message(self, who, msg):

        color = "#00ffff"

        if who.lower() == "you":
            color = "#ff00ff"

        self.chat.append(
            f"<font color='{color}'><b>{who}</b></font><br>{msg}<br><br>"
        )

    # ---------- STATUS ----------

    def set_status(self, text):
        self.status.setText(text)

    # ---------- AI STATES ----------

    # ---------------- AI STATES ---------------- #

    def listening(self):

        self.status.setText("🎤 LISTENING")
        self.core.set_state("listening")
        self.wave.start()


    def thinking(self):

        self.status.setText("🧠 THINKING")
        self.core.set_state("thinking")
        self.wave.stop()


    def speaking(self):

        self.status.setText("🗣 SPEAKING")
        self.core.set_state("speaking")
        self.wave.start()


    def ready(self):

        self.status.setText("🟢 READY")
        self.core.set_state("ready")
        self.wave.stop()


    def sleep(self):

        self.status.setText("😴 SLEEP")
        self.core.set_state("sleep")
        self.wave.stop()
        def resizeEvent(self, event):

            self.centralWidget().findChild(Background).setGeometry(self.centralWidget().rect())

            self.centralWidget().findChildren(QWidget)[1].setGeometry(
                self.centralWidget().rect()
            )

            super().resizeEvent(event)