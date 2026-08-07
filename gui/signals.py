from PySide6.QtCore import QObject, Signal


class GuiSignals(QObject):

    add_message = Signal(str, str)

    set_status = Signal(str)

    listening = Signal()

    thinking = Signal()

    speaking = Signal()

    ready = Signal()

    sleep = Signal()


signals = GuiSignals()