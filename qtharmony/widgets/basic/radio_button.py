from PySide6.QtWidgets import QRadioButton

from qtharmony.core import StyleSheetLoader
from qtharmony.core.theme import ThemeManager
from qtharmony.core.sizes import AbstractSize

from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class RadioButton(QRadioButton):
    """
    Custom QRadioButton widget for radio button functionality.

    Methods:
    - __init__(text: Optional[str] = None, size: tuple[int, int] = (200, 30),
              *, stylesheet: Optional[str] = None, parent: Optional["QWidget"] = None): None
              - Initializes the RadioButton widget with optional text, size, and stylesheet.
    """

    def __init__(
            self,
            text: Optional[str] = None,
            size: Optional[AbstractSize] = None,
            is_active: bool = True,
            *,
            object_name: str = "radio-button",
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        """
        Initializes the RadioButton widget with optional text, size, and stylesheet.

        Args:
            text (Optional[str], optional): The text displayed next to the radio button. Defaults to None.
            size (tuple[int, int], optional): The size of the radio button widget (width, height). Defaults to (200, 30).
            stylesheet (Optional[str], optional): Custom stylesheet for the radio button widget. Defaults to None.
            parent (Optional["QWidget"], optional): Parent widget of the radio button. Defaults to None.
        """ 

        super().__init__(parent)
        ThemeManager.add_widgets(self)

        self.setDisabled(not is_active)

        if text is not None: self.setText(text)
        if size is not None: size.use(self)

        self.setObjectName(object_name)
        self.stylesheet = StyleSheetLoader.load_stylesheet(
            __file__, "styles/radio_button.css", 
            name=self.__class__.__name__, obj_name=f"QRadioButton#{self.objectName()}",
            stylesheet=stylesheet
        )
