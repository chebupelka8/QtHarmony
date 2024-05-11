from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize

from qtharmony.src.core import StyleSheetLoader

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget
    from PySide6.QtGui import QFont


class PushButton(QPushButton):
    """
    Custom QPushButton widget for push button functionality.

    Methods:
    - __init__(text: Optional[str] = None, size: tuple[int, int] = (100, 25), 
              font: Optional["QFont"] = None, *, stylesheet: Optional[str] = None, 
              parent: Optional["QWidget"] = None): None
              - Initializes the PushButton widget with optional text, size, font, and stylesheet.

    """

    def __init__(
            self, 
            text: Optional[str] = None,
            size: tuple[int, int] = (100, 25),
            font: Optional["QFont"] = None, 
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None, 
    ) -> None:
        """
        Initializes the PushButton widget with optional text, size, font, and stylesheet.

        Args:
            text (Optional[str], optional): The text displayed on the push button. Defaults to None.
            size (tuple[int, int], optional): The size of the push button widget (width, height). Defaults to (100, 25).
            font (Optional["QFont"], optional): The font used for the push button text. Defaults to None.
            stylesheet (Optional[str], optional): Custom stylesheet for the push button widget. Defaults to None.
            parent (Optional["QWidget"], optional): Parent widget of the push button. Defaults to None.
        """ 


        super().__init__(parent)

        if font is not None: self.setFont(font)

        self.setStyleSheet(StyleSheetLoader.load_stylesheet(
            __file__, "styles/button.css", 
            name="PushButton", obj_name="QPushButton#button",
            stylesheet=stylesheet
        ))
        
        self.setObjectName("button")
        self.setFixedSize(QSize(*size))

        if text is not None:
            self.setText(text)
        
        if stylesheet is not None:
            self.setStyleSheet(self.styleSheet() + stylesheet)
