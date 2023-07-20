from PySide6.QtWidgets import QMainWindow, QPushButton, QSlider, QVBoxLayout, QWidget, QLabel, QToolBar, QApplication, QStatusBar, QMessageBox, QAbstractButton
from PySide6.QtCore import Qt, QSize, Slot
from PySide6.QtGui import QAction, QIcon, QPixmap


def big_problem():
    print("hello world")


def initlize_custom_message_box(title: str, description: str) -> QMessageBox:
    custom_message_box = QMessageBox()
    custom_message_box.setMinimumSize(700, 200)
    custom_message_box.setWindowTitle(title)
    custom_message_box.setText(title)
    custom_message_box.setInformativeText(description)
    custom_message_box.setIconPixmap(QPixmap("./braces-asterisk.svg"))
    custom_message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    custom_message_box.setDefaultButton(QMessageBox.Cancel)
    message_box_button = custom_message_box.addButton(
        "hello world", QMessageBox.ActionRole)
    message_box_button.clicked.disconnect()
    message_box_button.clicked.connect(big_problem)
    custom_message_box.addButton(
        "second world", QMessageBox.ButtonRole.AcceptRole)

    return custom_message_box


class MainWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()

        self.app = app
        self.setWindowTitle("Testing Grounds")
        # Main widget
        main_widget = MainWidget()
        self.setCentralWidget(main_widget)

    @Slot()
    def quit(self):
        self.app.quit()

    @Slot()
    def send_message(self):
        self.statusBar().showMessage("I'm loading please wait.", 1500)


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        button = QPushButton(text="Show Message box")
        button.clicked.connect(self.button_clicked)

        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)
        slider.valueChanged.connect(self.slider_value_change)

        self.widget_layout = QVBoxLayout()
        self.widget_layout.addWidget(button)
        self.widget_layout.addWidget(slider)
        self.setLayout(self.widget_layout)

    @Slot()
    def button_clicked(self):
        message_box: QMessageBox = initlize_custom_message_box(
            "This is the title", "some text just for the sake of having text :)")
        ret = message_box.exec()

        if ret == QMessageBox.Ok:
            print("Good")
        else:
            print("Not good")

    @Slot()
    def slider_value_change(self, value):
        print(value, type(value))


# # Menu bar
# main_menu = self.menuBar()
# file_menu = main_menu.addMenu("&File")
# quit_action = file_menu.addAction("Quit")
# quit_action.triggered.connect(self.quit)

# edit_menu = main_menu.addMenu("&Edit")
# edit_menu.addAction("Copy")
# edit_menu.addAction("Cut")
# edit_menu.addAction("Paste")
# edit_menu.addAction("Undo")
# edit_menu.addAction("Redo")

# main_menu.addMenu("&Window")
# main_menu.addMenu("&Settings")
# main_menu.addMenu("&Help")

# # ToolBar
# toolbar = QToolBar("My personal awesome toolbar")
# toolbar.setIconSize(QSize(16, 16))
# toolbar.setMovable(False)
# self.addToolBar(toolbar)

# main_action = QAction(QIcon("./trash3.svg"), "Awesome action", self)
# main_action.setStatusTip("This is so awesome, right?")
# toolbar.addAction(main_action)

# toolbar.addSeparator()
# close_button = QPushButton("Close App")
# close_button.clicked.connect(self.quit)
# toolbar.addWidget(close_button)

# toolbar.addSeparator()
# send_message = QPushButton("Active Message")
# send_message.clicked.connect(self.send_message)
# toolbar.addWidget(send_message)
# # Status bar
# self.setStatusBar(QStatusBar(self))
