from PySide6.QtWidgets import QLabel

from qtharmony.src.core import Font, StyleSheetLoader

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class Label(QLabel):
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
        self.__append_stylesheet("Label {" + f"color: {color}" + "}")
    
    def __append_stylesheet(self, stylesheet: str) -> None:
        self.setStyleSheet(StyleSheetLoader.append_stylesheet(
            self.styleSheet(), stylesheet, name="Label", obj_name="QLabel#label"
        ))
