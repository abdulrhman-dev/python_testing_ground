from PySide6.QtWidgets import QMainWindow, QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Qt
from pandas import read_excel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Testing grounds")
        self.setFixedWidth(850)

        file_dialog = QFileDialog(
            self, caption="Open Image", filter="XLSX File (*.xlsx)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        user_selected = file_dialog.exec()

        if (user_selected):
            working_file = file_dialog.selectedFiles()[0]

            df = read_excel(working_file)

            column_number, row_number = df.shape
            columns = list(df.columns)

            table_widget = QTableWidget(column_number, row_number, self)

            table_widget.setHorizontalHeaderLabels(columns)
            table_widget.verticalHeader().hide()

            table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

            for row_index, row in enumerate(df.to_dict('records')):
                for column_index, column in enumerate(columns):
                    table_widget.setItem(
                        row_index, column_index, QTableWidgetItem(str(row[column])))
            table_widget.selectRow(3645)
            self.setCentralWidget(table_widget)


def xlsx_analyizer(file_dir: str) -> None:
    dataframe = read_excel(file_dir)


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
