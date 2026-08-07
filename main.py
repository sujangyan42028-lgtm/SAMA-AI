import sys
import threading
from gui.waveform import Waveform
from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow
from core.assistant import run, set_window


def run_assistant():
    run()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    set_window(window)

    assistant = threading.Thread(
        target=run_assistant,
        daemon=True
    )
    assistant.start()

    sys.exit(app.exec())