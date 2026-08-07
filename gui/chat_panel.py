from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QTextEdit,
    QVBoxLayout
)


class ChatPanel(QFrame):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(420)

        layout = QVBoxLayout(self)

        title = QLabel("💬 CONVERSATION")

        title.setStyleSheet("""
        color:#00ffff;
        font-size:22px;
        font-weight:bold;
        padding:8px;
        """)

        layout.addWidget(title)

        self.chat = QTextEdit()

        self.chat.setReadOnly(True)

        self.chat.setStyleSheet("""
        QTextEdit{
            background:#10131d;
            color:white;
            border:2px solid #00ffff;
            border-radius:12px;
            padding:12px;
            font-size:15px;
        }
        """)

        layout.addWidget(self.chat)

    def add_user(self, text):

        self.chat.append(f"""
        <div style='color:#00ffff'>
        <b>👤 YOU</b><br>
        {text}
        </div><br>
        """)

    def add_ai(self, text):

        self.chat.append(f"""
        <div style='color:#ff00ff'>
        <b>🤖 SAMA</b><br>
        {text}
        </div><br>
        """)

        cursor = self.chat.textCursor()
        cursor.movePosition(cursor.End)
        self.chat.setTextCursor(cursor)