from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Wierd Text Editor")
        self.setMinimumSize(QSize(700, 500))

        main_widget = MainWidget()

        self.setCentralWidget(main_widget)


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()

        copy_button = QPushButton(QIcon('./icons/clipboard.svg'), "Copy")
        cut_button = QPushButton(QIcon('./icons/scissors.svg'), "Cut")
        paste_button = QPushButton(
            QIcon('./icons/clipboard2-fill.svg'), "Paste")
        undo_button = QPushButton(
            QIcon('./icons/arrow-counterclockwise.svg'), "Undo")
        redo_button = QPushButton(
            QIcon('./icons/arrow-clockwise.svg'), "Redo")
        plain_text_button = QPushButton(
            QIcon('./icons/file-text.svg'), "Set Plain Text")
        html_button = QPushButton(
            QIcon('./icons/filetype-html.svg'), "Set Html")
        clear_button = QPushButton(QIcon('./icons/trash3.svg'), "Clear")

        self.text_edit = QTextEdit()

        # connections
        copy_button.clicked.connect(self.text_edit.copy)
        cut_button.clicked.connect(self.text_edit.cut)
        paste_button.clicked.connect(self.text_edit.paste)
        undo_button.clicked.connect(self.text_edit.undo)
        redo_button.clicked.connect(self.text_edit.redo)
        html_button.clicked.connect(self.button_to_html)
        plain_text_button.clicked.connect(self.button_plain_text)
        clear_button.clicked.connect(self.text_edit.clear)

        button_layout = QHBoxLayout()
        button_layout.addWidget(copy_button)
        button_layout.addWidget(cut_button)
        button_layout.addWidget(paste_button)
        button_layout.addWidget(undo_button)
        button_layout.addWidget(redo_button)
        button_layout.addWidget(plain_text_button)
        button_layout.addWidget(html_button)
        button_layout.addWidget(clear_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.text_edit)

        self.setLayout(main_layout)

    def button_plain_text(self):
        self.text_edit.setPlainText(self.text_edit.toPlainText())

    def button_to_html(self):
        self.text_edit.setText(self.text_edit.toPlainText())
