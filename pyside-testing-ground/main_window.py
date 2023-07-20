from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtCore import Slot


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Line Edit Test")

        main_widget = MainWidget()
        self.setCentralWidget(main_widget)


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()

        line_edit_label = QLabel("Enter something: ")

        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.handle_text_change)
        self.line_edit.textEdited.connect(self.handle_text_edit)

        confirm_button = QPushButton("Do Amazing things")
        confirm_button.clicked.connect(self.change_text)

        self.output_label = QLabel("I'm nothing but a mere placeholder")

        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()

        input_layout.addWidget(line_edit_label)
        input_layout.addWidget(self.line_edit)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(confirm_button)
        main_layout.addWidget(self.output_label)

        self.setLayout(main_layout)

    @Slot()
    def change_text(self):
        self.output_label.setText(self.line_edit.text())

    # @Slot()
    # def handle_text_change(self, value):
    #     print(value)

    # @Slot()
    # def handle_text_edit(self, value):
    #     print(value)
