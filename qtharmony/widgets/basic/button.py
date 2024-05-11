from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize

from qtharmony.src.core import Loader, StyleSheetLoader

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

        self.setStyleSheet(StyleSheetLoader.load_stylesheet(
            __file__, "styles/button.css", 
            name="PushButton", obj_name="QPushButton#button",
            stylesheet=stylesheet
        ))
        
        self.setObjectName("button")
        self.setMinimumSize(QSize(*size))

        if text is not None:
            self.setText(text)
        
        if stylesheet is not None:
            self.setStyleSheet(self.styleSheet() + stylesheet)
