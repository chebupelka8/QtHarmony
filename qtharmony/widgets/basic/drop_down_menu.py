import os.path

from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import Qt, QSize

from qtharmony.src.core import StyleSheetLoader
from qtharmony.src.util import RESOURCES

from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from PySide6.QtGui import QFont
    from PySide6.QtWidgets import QWidget


class DropDownMenu(QComboBox):
    """
    Custom QComboBox widget for displaying a drop-down menu.

    Methods:
    - __init__(*__values: str, width: int = 200, height: int = 25): None - Initializes the drop-down menu with specified values, width, and height.
    - set_items(*__values: str): None - Sets the items in the drop-down menu.
    """

    def __init__(
            self, 
            values: Optional[list[str]] = None, 
            size: tuple[int, int] = (200, 30),
            font: Optional["QFont"] = None, 
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        self.setFixedSize(QSize(*size))
        self.view().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.__values = []

        if values is not None: self.__values = [*values]
        self.addItems(self.__values)
        self.setObjectName("drop-down-menu")
        if font is not None: self.setFont(font)

        self.setStyleSheet(StyleSheetLoader.load_stylesheet(
            __file__, "styles/drop_down_menu.css", 
            name="DropDownMenu", obj_name="QComboBox#drop-down-menu",
            stylesheet=stylesheet
        ))

        self.__load_down_arrow_style()
    
    def __load_down_arrow_style(self) -> None:
        down_arrow = (
            "\nDropDownMenu::down-arrow {" 
            + f"image: url({os.path.join(RESOURCES, 'ui/angle-down.png')})" 
            + "}"
        )

        self.setStyleSheet(StyleSheetLoader.append_stylesheet(
            self.styleSheet(), down_arrow, 
            name="DropDownMenu", obj_name="QComboBox#drop-down-menu"
        ))

    def set_items(self, *__values: str) -> None:
        self.__values = [*__values]
        self.addItems(self.__values)

