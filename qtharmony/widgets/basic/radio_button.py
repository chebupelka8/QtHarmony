from PySide6.QtWidgets import QRadioButton
from PySide6.QtCore import QSize

from qtharmony.src.core import StyleSheetLoader
from qtharmony.src.util import RESOURCES

from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class RadioButton(QRadioButton):
    def __init__(
            self,
            text: Optional[str] = None,
            size: tuple[int, int] = (200, 30),
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        if text is not None: self.setText(text)
        self.setFixedSize(QSize(*size))

        self.setObjectName("radio-button")
        self.setStyleSheet(StyleSheetLoader.load_stylesheet(
            __file__, "styles/radio_button.css", 
            name="RadioButton", obj_name="QRadioButton#radio-button",
            stylesheet=stylesheet
        ))
