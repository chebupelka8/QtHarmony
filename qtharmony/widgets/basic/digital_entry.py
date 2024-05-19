from PySide6.QtWidgets import QSpinBox
from PySide6.QtCore import QSize

from qtharmony.core import StyleSheetLoader
from qtharmony.core.theme import ThemeManager
from qtharmony.core.sizes import AbstractSize

from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from PySide6.QtGui import QFont
    from PySide6.QtWidgets import QWidget


class DigitalEntry(QSpinBox):
    """
    Custom QSpinBox widget for numerical input.

    Methods:
    - __init__(range: tuple[int, int] = (0, 100), size: tuple[int, int] = (40, 30),
              font: Optional["QFont"] = None, include_buttons: bool = False,
              *, stylesheet: Optional[str] = None, parent: Optional["QWidget"] = None): None
              - Initializes the DigitalEntry widget with optional range, size, font, button inclusion, and stylesheet.
    """

    def __init__(
            self, 
            range: tuple[int, int] = (0, 100), 
            size: Optional[AbstractSize] = None,
            font: Optional["QFont"] = None, 
            include_buttons: bool = False,
            is_active: bool = True,
            *,
            object_name: str = "digital-entry",
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        """
        Initializes the DigitalEntry widget with optional range, size, font, button inclusion, and stylesheet.

        Args:
            range (tuple[int, int], optional): The range of values allowed in the spin box. Defaults to (0, 100).
            size (tuple[int, int], optional): The size of the spin box widget (width, height). Defaults to (40, 30).
            font (Optional["QFont"], optional): The font to be used for text input. Defaults to None.
            include_buttons (bool, optional): Flag to include or exclude spin box buttons. Defaults to False.
            stylesheet (Optional[str], optional): Custom stylesheet for the spin box widget. Defaults to None.
            parent (Optional["QWidget"], optional): Parent widget of the spin box. Defaults to None.
        """

        super().__init__(parent)
        ThemeManager.add_widgets(self)

        if size is not None: size.use(self)
        if not include_buttons: self.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        if font is not None: self.setFont(font)
        self.setDisabled(not is_active)

        self.setObjectName(object_name)
        self.setRange(*range)

        self.stylesheet = StyleSheetLoader.load_stylesheet(
            __file__, "styles/digital_entry.css", 
            name=self.__class__.__name__, obj_name=f"QSpinBox#{self.objectName()}",
            stylesheet=stylesheet
        )
