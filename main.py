from PySide6.QtWidgets import (
    QWidget, QHBoxLayout
)

import sys

from qtharmony.widgets import *
from qtharmony.windows import MainWindow
from qtharmony.constructor import Initialization
from qtharmony.src.core.theme import ThemeManager


Initialization.init(sys.argv)
ThemeManager.change_theme("Dark-Green")


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.mainLayout = QHBoxLayout()

        group = GroupBox("GroupBox")
        group.addWidget(RadioButton("RadioButton 1"))
        group.addWidget(RadioButton("RadioButton 2"))
        group.addWidget(RadioButton("RadioButton 3"))

        self.mainLayout.addWidget(PushButton("Button"))
        
        self.mainLayout.addWidget(group)

        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    window = MainWindow(Window())
    window.run()

    Initialization.exec()
