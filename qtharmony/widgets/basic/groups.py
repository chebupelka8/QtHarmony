from typing import Optional, TYPE_CHECKING

from PySide6.QtWidgets import (
    QGroupBox, QButtonGroup
)

from qtharmony.src.core import Loader, StyleSheetLoader

import os.path

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class GroupBox(QGroupBox):
    """
    Custom QGroupBox widget for grouping widgets.

    Methods:
    - __init__(title: Optional[str] = None, *, stylesheet: Optional[str] = None, parent: Optional["QWidget"] = None): None
              - Initializes the GroupBox widget with optional title and stylesheet.
    """

    def __init__(
            self,
            title: Optional[str] = None,
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        """
        Initializes the GroupBox widget with optional title and stylesheet.

        Args:
            title (Optional[str], optional): The title of the group box. Defaults to None.
            stylesheet (Optional[str], optional): Custom stylesheet for the group box widget. Defaults to None.
            parent (Optional["QWidget"], optional): Parent widget of the group box. Defaults to None.
        """

        super().__init__(parent)

        self.setObjectName("group-box")
        self.setStyleSheet(StyleSheetLoader.load_stylesheet(
            __file__, "styles/group_box.css", 
            name="GroupBox", obj_name="QGroupBox#group-box",
            stylesheet=stylesheet
        ))

        if title is not None: self.setTitle(title)
