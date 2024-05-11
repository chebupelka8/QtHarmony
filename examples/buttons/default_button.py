from qtharmony.constructor import Initialization
from qtharmony.windows import MainWindow
from qtharmony.widgets import PushButton

from PySide6.QtWidgets import QWidget, QHBoxLayout

import sys


Initialization.init(sys.argv)


class Widget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(PushButton("Button"))
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    window = MainWindow(widget=Widget(), title="Hello", size=(600, 400))
    window.run()

    Initialization.exec()