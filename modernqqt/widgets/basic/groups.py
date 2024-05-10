from typing import Optional, TYPE_CHECKING

from PySide6.QtWidgets import (
    QGroupBox, QButtonGroup
)

from modernqqt.src.core import Loader

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
        stylesheet_path = os.path.join(os.path.dirname(__file__), "styles/group_box.css")

        if stylesheet is not None:
            self.setStyleSheet(
                Loader.load_file(stylesheet_path) + "\n" 
                + stylesheet.replace("GroupBox", "QGroupBox#group-box")
            )
        else:
            self.setStyleSheet(Loader.load_file(stylesheet_path))


        if title is not None: self.setTitle(title)
