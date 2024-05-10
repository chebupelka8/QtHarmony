from PySide6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QLabel
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

import sys

from modernqqt.widgets import *
# from src.core import Font


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowIcon(QIcon("Icon.png"))
        self.setWindowTitle("ModernQt")

        self.resize(1000, 600)
        self.setStyleSheet("background-color: #fbfbfb")

        self.widgetsList = WidgetsList()

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(PushButton("Button"))

        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
