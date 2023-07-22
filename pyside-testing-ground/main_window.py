from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QFrame, QGroupBox, QGridLayout, QSizePolicy, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QRadioButton
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Testing grounds")

        main_widget = MainWidget()
        self.setCentralWidget(main_widget)


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Widgets
        line_label = QLabel()
        line_label.setText("Enter some Info")
        line_edit = QLineEdit()

        first_button = QPushButton("first option")
        second_button = QPushButton("second option")
        third_button = QPushButton("third option")

        option_a = QRadioButton("A")
        option_b = QRadioButton("B")
        option_c = QRadioButton("C")
        option_a.setChecked(True)

        # Registering Slots
        option_a.toggled.connect(self.option_a_selected)
        option_b.toggled.connect(self.option_b_selected)
        option_c.toggled.connect(self.option_c_selected)

        # Boxes
        radio_group_box = QGroupBox("اختر خيار ما")
        radio_group_box.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        radio_group_box.setAlignment(Qt.AlignmentFlag.AlignRight)

        button_frame = QFrame()
        button_frame.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)

        line_frame = QFrame()
        line_frame.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        # Layouts
        grid_layout = QGridLayout()
        button_layout = QVBoxLayout()

        button_layout.addWidget(first_button)
        button_layout.addWidget(second_button)
        button_layout.addWidget(third_button)
        button_frame.setLayout(button_layout)

        label_layout = QVBoxLayout()
        label_layout.addWidget(line_label)
        label_layout.addWidget(line_edit)
        label_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        line_frame.setLayout(label_layout)

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(option_a)
        radio_layout.addWidget(option_b)
        radio_layout.addWidget(option_c)
        radio_group_box.setLayout(radio_layout)

        grid_layout.addWidget(button_frame, 0, 0)
        grid_layout.addWidget(line_frame, 0, 1)
        grid_layout.addWidget(radio_group_box, 1, 0, 1, 2)

        self.setLayout(grid_layout)

    def option_a_selected(self, checked):
        if checked:
            print("Option a checked")
        else:
            print("Option a unchecked")

    def option_b_selected(self, checked):
        if checked:
            print("Option b checked")
        else:
            print("Option b unchecked")

    def option_c_selected(self, checked):
        if checked:
            print("Option c checked")
        else:
            print("Option c unchecked")
