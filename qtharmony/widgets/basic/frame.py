from PySide6.QtWidgets import QFrame

from qtharmony.core import StyleSheetLoader
from qtharmony.core.theme import ThemeManager
from qtharmony.core.sizes import AbstractSize

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class Frame(QFrame):

    def __init__(
            self,
            size: Optional[AbstractSize] = None,
            is_active: bool = True,
            *,
            object_name: str = "frame",
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)
        ThemeManager.add_widgets(self)

        self.setObjectName(object_name)
        self.stylesheet = StyleSheetLoader.load_stylesheet(
            __file__, "styles/frame.css", 
            name=self.__class__.__name__, obj_name=f"QFrame#{self.objectName()}",
            stylesheet=stylesheet
        )

        self.setDisabled(not is_active)

        if size is not None:
            size.use(self)

