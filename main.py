from PySide6.QtWidgets import (
    QWidget, QHBoxLayout
)
from PySide6.QtCore import Qt

import sys

from qtharmony.widgets import *
from qtharmony.windows import MainWindow
from qtharmony.constructor import Initialization
from qtharmony.src.core.theme import ThemeManager


Initialization.init(sys.argv)


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.mainLayout = QHBoxLayout()

        self.mainLayout.addWidget(Label("Hello", "Noto Sans", 14, color="#000", stylesheet="Label {color: blue}"))

        btn = PushButton("Click to change theme", size=(200, 35), stylesheet="PushButton {background-color: lightgreen}")
        btn.clicked.connect(lambda: ThemeManager.change_theme("Light-Default"))

        self.mainLayout.addWidget(btn)

        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    window = MainWindow(Window())
    window.run()

    Initialization.exec()
