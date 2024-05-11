from PySide6.QtWidgets import (
    QWidget, QHBoxLayout
)

import sys

from qtharmony.widgets import *
from qtharmony.windows import MainWindow
from qtharmony.constructor import Initialization

Initialization.init(sys.argv)


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.widgetsList = WidgetsList()

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(PathEntry())
        self.mainLayout.addWidget(PushButton())

        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    window = MainWindow(Window())
    window.run()

    Initialization.exec()
