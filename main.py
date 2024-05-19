from PySide6.QtWidgets import (
    QWidget, QHBoxLayout
)

import sys

from qtharmony.widgets import *
from qtharmony.windows import MainWindow
from qtharmony.constructor import Initialization
from qtharmony.core.theme import ThemeManager
from qtharmony.core.sizes import *


Initialization.init(sys.argv)
# ThemeManager.change_theme("Dark-Green")


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.mainLayout = QHBoxLayout()

        # self.mainLayout.addWidget(PushButton("hello", SizeGroup(MinimalSize(height=100), MaximalSize(width=100))))
        # self.mainLayout.addWidget(PictureWidget("qtharmony/resources/ui/Icon.png"))
        self.mainLayout.addWidget(TextBox(placeholder="Type smth..."))

        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    window = MainWindow(Window())
    window.run()

    Initialization.exec()
