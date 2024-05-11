from PySide6.QtWidgets import (
    QWidget, QHBoxLayout
)

import sys

from qtharmony.widgets import *
from qtharmony.windows import MainWindow
from qtharmony.constructor import Initialization

from qtharmony.src.core.theme import ThemeBuilder, ThemeManager

Initialization.init(sys.argv)


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.widgetsList = WidgetsList()

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(Label("Hello", "Noto Sans", 13))
        self.mainLayout.addWidget(PushButton("Button"))
        self.mainLayout.addWidget(DropDownMenu([str(i) for i in range(100)]))

        self.setLayout(self.mainLayout)

        print(ThemeManager.get_widgets())
        ThemeManager.update()


if __name__ == "__main__":
    window = MainWindow(Window())
    window.show()

    Initialization.exec()
