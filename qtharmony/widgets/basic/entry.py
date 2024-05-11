from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, QSize

from qtharmony.src.core import StyleSheetLoader

from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from PySide6.QtGui import QFont
    from PySide6.QtWidgets import QWidget


class Entry(QLineEdit):
    """
    Custom QLineEdit widget for text entry.

    Methods:
    - __init__(__placed: str, placeholder: str = "", width: int = 200, height: int = 25): None - Initializes the text entry with default text and placeholder.
    """

    def __init__(
            self, 
            placed: Optional[str] = None, 
            placeholder: Optional[str] = None,
            size: tuple[int, int] = (200, 30), 
            font: Optional["QFont"] = None, 
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        if placed is not None: self.setText(placed)
        if placeholder is not None: self.setPlaceholderText(placeholder)
        if font is not None: self.setFont(font)

        self.setFixedSize(QSize(*size))
        self.setObjectName("entry")
        self.setFocusPolicy(Qt.FocusPolicy.WheelFocus)

        self.setStyleSheet(StyleSheetLoader.load_stylesheet(
            __file__, "styles/entry.css", 
            name="Entry", obj_name="QLineEdit#entry",
            stylesheet=stylesheet
        ))

