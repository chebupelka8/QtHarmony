from PySide6.QtWidgets import QLabel

from qtharmony.src.core import Font, StyleSheetLoader

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class Label(QLabel):
    """
    Custom QLabel widget for displaying text.

    Methods:
    - __init__(text: str, font_family: str, font_size: int, bold: bool = False, italic: bool = False, color: str = "#000000",
              word_wrap: bool = False, *, stylesheet: Optional[str] = None, parent: Optional["QWidget"] = None): None
              - Initializes the Label widget with optional text, font family, font size, bold, italic, color, word wrap, and stylesheet.
    - set_color(self, color: str) -> None
              - Sets the color of the label text.
    - __append_stylesheet(self, stylesheet: str) -> None
              - Appends a custom stylesheet to the label widget.
    """

    def __init__(
            self, 
            text: str,
            font_family: str, 
            font_size: int,
            bold: bool = False,
            italic: bool = False,
            color: str = "#000000",
            word_wrap: bool = False,
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        """
        Initializes the Label widget with optional text, font family, font size, bold, italic, color, word wrap, and stylesheet.

        Args:
            text (str): The text to be displayed in the label.
            font_family (str): The font family to be used for the label text.
            font_size (int): The font size to be used for the label text.
            bold (bool, optional): Flag to make the label text bold. Defaults to False.
            italic (bool, optional): Flag to make the label text italic. Defaults to False.
            color (str, optional): The color of the label text. Defaults to "#000000".
            word_wrap (bool, optional): Flag to enable word wrap for the label text. Defaults to False.
            stylesheet (Optional[str], optional): Custom stylesheet for the label widget. Defaults to None.
            parent (Optional["QWidget"], optional): Parent widget of the label. Defaults to None.
        """

        super().__init__(parent)

        self.setObjectName("label")
        self.setStyleSheet(StyleSheetLoader.load_stylesheet(
            __file__, "styles/label.css", 
            name="Label", obj_name="QLabel#label",
            stylesheet=stylesheet
        ))

        self.setText(text)
        self.set_color(color)
        
        self.setWordWrap(word_wrap)
        self.setFont(Font.get_system_font(font_family, font_size, bold, italic))
    
    def set_color(self, color: str) -> None:
        """
        Sets the color of the label text.

        Args:
            color (str): The color of the label text.
        """

        self.__append_stylesheet("Label {" + f"color: {color}" + "}")
    
    def __append_stylesheet(self, stylesheet: str) -> None:
        """
        Appends a custom stylesheet to the label widget.

        Args:
            stylesheet (str): The custom stylesheet to be appended.
        """

        self.setStyleSheet(StyleSheetLoader.append_stylesheet(
            self.styleSheet(), stylesheet, name="Label", obj_name="QLabel#label"
        ))
