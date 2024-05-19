from typing import Optional, TYPE_CHECKING

from PySide6.QtWidgets import (
    QListWidget, QListWidgetItem, QFrame,
    QHBoxLayout
)
from PySide6.QtCore import Qt

from qtharmony.core import StyleSheetLoader
from qtharmony.core.theme import ThemeManager
from qtharmony.core.sizes import AbstractSize

from .label import Label

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class WidgetsList(QListWidget):
    """
    now is in development.
    should not use.
    """

    def __init__(
            self, 
            size: Optional[AbstractSize] = None,
            title: Optional[str] = None,
            is_active: bool = True,
            *,
            object_name: str = "widgets-list",
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None,
    ) -> None:
        super().__init__(parent)
        ThemeManager.add_widgets(self)
    
        if size is not None: size.use(self)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setDisabled(not is_active)

        self.setObjectName(object_name)
        self.stylesheet = StyleSheetLoader.load_stylesheet(
            __file__, "styles/widgets_list.css",
            name=self.__class__.__name__, obj_name=f"QListWidget#{self.objectName()}",
            stylesheet=stylesheet
        )

    def add_widget(self, widget) -> None:
        item = QListWidgetItem()
        self.addItem(item)
        self.setItemWidget(item, widget)
