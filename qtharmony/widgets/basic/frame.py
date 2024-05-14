from PySide6.QtWidgets import QFrame

from qtharmony.src.core import StyleSheetLoader
from qtharmony.src.core.theme import ThemeManager

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class Frame(QFrame):

    def __init__(
            self,
            size: Optional[tuple[int, int]] = None,
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)
        ThemeManager.add_widgets(self)

        self.stylesheet = StyleSheetLoader.load_stylesheet(
            __file__, "styles/button.css", 
            name=self.__class__.__name__, obj_name="QFrame#frame",
            stylesheet=stylesheet
        )
        self.setObjectName("frame")

        if size is not None:
            self.setFixedSize(*size)

