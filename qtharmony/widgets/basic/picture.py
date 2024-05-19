from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap

from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from PySide6.QtGui import QPixmap, QImage


class PictureWidget(QLabel):
    def __init__(self, image: Union["QPixmap", str, "QImage"]) -> None:
        super().__init__()

        self.setPixmap(QPixmap(image))
        self.resize(self.pixmap().size())
