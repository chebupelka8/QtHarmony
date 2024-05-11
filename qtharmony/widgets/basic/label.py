from PySide6.QtWidgets import QLabel

from qtharmony.src.core import Font

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

        self.setText(text)
        self.setStyleSheet("QLabel#label {" f"color: {color}" + "}")
        if stylesheet is not None: self.setStyleSheet(self.styleSheet() + "\n" + stylesheet.replace("Label", "QLabel#label"))
        self.setWordWrap(word_wrap)
        self.setFont(Font.get_system_font(font_family, font_size, bold, italic))
