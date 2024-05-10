from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize

from modernqqt.src.core import Loader

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget
    from PySide6.QtGui import QFont

import os.path


class PushButton(QPushButton):
    def __init__(
            self, 
            text: Optional[str] = None,
            size: tuple[int, int] = (100, 25),
            font: Optional["QFont"] = None, 
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None, 
    ) -> None:
        super().__init__(parent)

        if font is not None: self.setFont(font)

        stylesheet_path = os.path.join(os.path.dirname(__file__), "styles/button.css")

        if stylesheet is not None:
            self.setStyleSheet(
                Loader.load_file(stylesheet_path) + "\n" 
                + stylesheet.replace("PushButton", "QPushButton#button")
            )
        else:
            self.setStyleSheet(Loader.load_file(stylesheet_path))
        
        self.setObjectName("button")
        self.setMinimumSize(QSize(*size))

        if text is not None:
            self.setText(text)
        
        if stylesheet is not None:
            self.setStyleSheet(self.styleSheet() + stylesheet)
