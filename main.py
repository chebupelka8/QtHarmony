from PySide6.QtWidgets import (
    QWidget, QHBoxLayout
)
from PySide6.QtCore import Qt

import sys

from qtharmony.widgets import *
from qtharmony.windows import MainWindow
from qtharmony.constructor import Initialization

Initialization.init(sys.argv)


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.widgetsList = WidgetsList()

        hbox = QHBoxLayout()
        hbox.addWidget(RadioButton("1"), alignment=Qt.AlignmentFlag.AlignHCenter)
        hbox.addWidget(RadioButton("2"), alignment=Qt.AlignmentFlag.AlignHCenter)
        hbox.addWidget(RadioButton("3"), alignment=Qt.AlignmentFlag.AlignHCenter)

        self.mainLayout = QHBoxLayout()
        self.groupBox = GroupBox("This is GroupBox")
        self.groupBox.setLayout(hbox)

        self.mainLayout.addWidget(self.groupBox)

        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    window = MainWindow(Window())
    window.run()

    Initialization.exec()
