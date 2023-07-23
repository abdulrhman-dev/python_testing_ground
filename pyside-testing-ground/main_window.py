from PySide6.QtWidgets import QWidget, QMainWindow
from PySide6.QtGui import QIcon
from design.ui_sample_window import Ui_Form

import design.resource_rc


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        main_widget = MainWidget()

        self.setWindowTitle("QtDesigner test")
        self.setCentralWidget(main_widget)


class MainWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
