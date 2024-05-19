from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

from qtharmony.core import StyleSheetLoader
from qtharmony.core.theme import ThemeManager
from qtharmony.core.sizes import AbstractSize

from typing import Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget
    from PySide6.QtGui import QFont, QPixmap


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
            size: Optional[AbstractSize] = None,
            font: Optional["QFont"] = None, 
            is_active: bool = True,
            icon: Optional[Union[str, "QIcon", "QPixmap"]] = None,
            icon_size: Optional[tuple[int, int]] = None,
            *,
            object_name: str = "button",
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
        ThemeManager.add_widgets(self)

        if icon is not None: 
            if isinstance(icon, str):
                self.setIcon(QIcon(icon))
            else:
                self.setIcon(icon)
        
        if icon_size is not None:
            self.setIconSize(QSize(*icon_size))

        if font is not None: self.setFont(font)
        self.setDisabled(not is_active)

        self.setObjectName(object_name)
        self.stylesheet = StyleSheetLoader.load_stylesheet(
            __file__, "styles/button.css", 
            name=self.__class__.__name__, obj_name=f"QPushButton#{self.objectName()}",
            stylesheet=stylesheet
        )
        
        if size is not None: size.use(self)

        if text is not None:
            self.setText(text)
        
        if stylesheet is not None:
            self.setStyleSheet(self.styleSheet() + stylesheet)
