from PySide6.QtWidgets import QSpinBox
from PySide6.QtCore import QSize

from qtharmony.src.core import StyleSheetLoader

from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from PySide6.QtGui import QFont
    from PySide6.QtWidgets import QWidget


class DigitalEntry(QSpinBox):
    """
    Custom QSpinBox widget for entering digital values.

    Methods:
    - __init__(__range: tuple[int, int], width: int = 30, height: int = 25, show_buttons: bool = False): None - Initializes the digital entry with a specified range, width, height, and button display.
    """

    def __init__(
            self, 
            range: tuple[int, int] = (0, 100), 
            size: tuple[int, int] = (40, 30), 
            font: Optional["QFont"] = None, 
            include_buttons: bool = False,
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        self.setFixedSize(QSize(*size))
        if not include_buttons: self.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        if font is not None: self.setFont(font)

        self.setObjectName("digital-entry")
        self.setRange(*range)

        self.setStyleSheet(StyleSheetLoader.load_stylesheet(
            __file__, "styles/digital_entry.css", 
            name="DigitalEntry", obj_name="QSpinBox#digital-entry",
            stylesheet=stylesheet
        ))

