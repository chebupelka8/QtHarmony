from PySide6.QtWidgets import (
    QWidget, QHBoxLayout
)

import sys

from modernqqt.widgets import *
from modernqqt.windows import MainWindow
from modernqqt.constructor import Initialization

Initialization.init(sys.argv)


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.widgetsList = WidgetsList()

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(PushButton("Button"))

        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    window = MainWindow(Window())
    window.show()

    Initialization.exec()
