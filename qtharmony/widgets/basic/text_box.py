from PySide6.QtWidgets import QPlainTextEdit, QTextEdit
from PySide6.QtCore import Qt

from qtharmony.core import StyleSheetLoader
from qtharmony.core.theme import ThemeManager
from qtharmony.core.sizes import AbstractSize

from typing import Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget
    from PySide6.QtGui import QFont


class TextBox(QPlainTextEdit):
    def __init__(
            self,
            placed: Optional[str] = None,
            placeholder: Optional[str] = None,
            size: Optional[AbstractSize] = None,
            font: Optional["QFont"] = None,
            is_active: bool = True,
            wrap: bool = False,
            *,
            object_name: str = "text-box",
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)
        ThemeManager.add_widgets(self)

        if placed is not None: self.setPlainText(placed)
        if placeholder is not None: self.setPlaceholderText(placeholder)
        if size is not None: size.use(self)
        if font is not None: self.setFont(font)
        self.setDisabled(not is_active)
        if not wrap: self.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self.setObjectName(object_name)
        self.stylesheet = StyleSheetLoader.load_stylesheet(
            __file__, "styles/text_box.css", 
            name=self.__class__.__name__, obj_name=f"QPlainTextEdit#{self.objectName()}",
            stylesheet=stylesheet
        )
