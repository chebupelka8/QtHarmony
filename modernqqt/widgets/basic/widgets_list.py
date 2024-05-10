from typing import Optional, TYPE_CHECKING

from PySide6.QtWidgets import (
    QListWidget, QListWidgetItem, QFrame,
    QHBoxLayout, QLabel
)
from PySide6.QtCore import Qt

from modernqqt.src.core import Loader

import os.path

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class WidgetsList(QFrame):
    def __init__(
            self, 
            size: tuple[int, int] = (600, 400),
            title: Optional[str] = None,
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None,
    ) -> None:
        super().__init__(parent)

        self.mainLayout = QHBoxLayout()
        self.listWidget = QListWidget()

        # self.setStyleSheet(Loader.load_file("modernqt/widgets/basic/styles/widgets_list.css"))
        self.setObjectName("widgets-list")
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        stylesheet_path = os.path.join(os.path.dirname(__file__), "styles/widgets_list.css")

        if stylesheet is not None:
            self.setStyleSheet(
                Loader.load_file(stylesheet_path) + "\n" 
                + stylesheet.replace("WidgetsList", "QListWidget#widgets-list")
            )
        else:
            self.setStyleSheet(Loader.load_file(stylesheet_path))

        if stylesheet is not None:
            self.setStyleSheet(self.styleSheet() + stylesheet)

    def add_widget(self, widget) -> None:
        item = QListWidgetItem()
        item.setSizeHint(widget.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, widget)