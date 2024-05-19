from PySide6.QtWidgets import QScrollBar
from PySide6.QtCore import Qt

from qtharmony.core import StyleSheetLoader
from qtharmony.core.sizes import AbstractSize
from qtharmony.core.theme import ThemeManager

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class ScrollBar(QScrollBar):
    def __init__(
            self,
            __orientation: str,
            size: Optional[AbstractSize] = None,
            *,
            object_name: str = "scroll-bar",
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        if __orientation == "horizontal": super().__init__(Qt.Orientation.Horizontal, parent)
        elif __orientation == "vertical": super().__init__(Qt.Orientation.Vertical, parent)

        ThemeManager.add_widgets(self)

        if size is not None: size.use(self)

        self.setObjectName(object_name)
        self.stylesheet = StyleSheetLoader.load_stylesheet(
            __file__, "styles/scrollbar.css", 
            name=self.__class__.__name__, obj_name=f"QScrollBar#{self.objectName()}",
            stylesheet=stylesheet
        )
