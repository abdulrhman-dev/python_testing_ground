from PySide6.QtCore import QSize, Qt, QTimer
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QLabel, QApplication, QSlider, QGraphicsDropShadowEffect
from PySide6.QtGui import QPixmap, QFont


class MainWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        self.setMinimumSize(QSize(630, 360))
        self.setWindowTitle("Image Tester")

        main_widget = MainWidget()
        self.setCentralWidget(main_widget)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.showFullScreen()
        self.setFixedSize(self.screen().size())


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.screen_size = self.screen().size()

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: blue;')

        self.image = QLabel(self)
        image_pixmap = QPixmap('./images/background-test-2.jpg')
        image_pixmap.scaled(self.screen_size.width() - 500, self.screen_size.height(),
                            aspectMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.image.setPixmap(image_pixmap)

        self.image.setScaledContents(True)

        mod = 0.5

        self.image.resize(self.screen_size.width() * mod,
                          self.screen_size.height() * mod)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animation)
        self.timer.setInterval(10)

        self.count_down = 3

        self.count_down_timer = QTimer(self)
        self.count_down_timer.timeout.connect(self.count_down_timeout)
        self.count_down_timer.setInterval(1000)

        self.count_down_text = QLabel(str(self.count_down), self)
        self.count_down_text.move(self.screen_size.width() / 2, 15)
        self.count_down_text.setFont(QFont("Arial", 45))
        self.count_down_text.setStyleSheet(
            "color: white; background-image: url(./images/clock.png); background-repeat: no-repeat;")
        self.count_down_text.setScaledContents(True)
        self.count_down_text.resize(151, 151)

        self.count_down_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.timer.start()
        self.count_down_timer.start()

    def animation(self):
        image_size = self.image.size()
        self.image.move(self.image.geometry().x() + 5.12,
                        self.screen_size.height() / 2 - (image_size.height() / 2))

        max_boundary = self.screen_size.width() - (image_size.width())
        if (self.image.geometry().x() > max_boundary):
            self.timer.stop()
            self.setStyleSheet('background-color: red;')

    def count_down_timeout(self):
        if self.count_down == 0:
            self.count_down_timer.stop()
            return

        self.count_down -= 1
        self.count_down_text.setText(str(self.count_down))
