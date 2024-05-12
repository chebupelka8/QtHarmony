from PySide6.QtWidgets import QFrame

from qtharmony.src.core import StyleSheetLoader
from qtharmony.src.core.theme import ThemeManager

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class Frame(QFrame):

    def __init__(
            self,
            size: tuple[int, int] = (600, 400),
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)
        ThemeManager.add_widgets(self)

        self.stylesheet = StyleSheetLoader.load_stylesheet(
            __file__, "styles/button.css", 
            name="Frame", obj_name="QFrame#frame",
            stylesheet=stylesheet
        )
        self.setObjectName("frame")

        self.setFixedSize(*size)

