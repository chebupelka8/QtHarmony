from typing import Optional, TYPE_CHECKING

from PySide6.QtWidgets import (
    QGroupBox, QButtonGroup
)

from qtharmony.src.core import Loader, StyleSheetLoader

import os.path

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class GroupBox(QGroupBox):
    def __init__(
            self,
            title: Optional[str] = None,
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        self.setObjectName("group-box")
        self.setStyleSheet(StyleSheetLoader.load_stylesheet(
            __file__, "styles/group_box.css", 
            name="GroupBox", obj_name="QGroupBox#group-box",
            stylesheet=stylesheet
        ))

        if title is not None: self.setTitle(title)
