import os.path

from PySide6.QtWidgets import ( 
    QWidget, QHBoxLayout, 
    QSpacerItem, QSizePolicy
)

from qtharmony.src.core import FileDialog, StyleSheetLoader

from .button import PushButton
from .entry import Entry

from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from PySide6.QtGui import QFont


class PathEntry(QWidget):
    """
    Custom QLineEdit widget for entering path to file and directories.

    Methods:
    - __init__(self, __placed: str, placeholder: str = "", width: int = 400, height: int = 25): None - Initializes the path entry with default text and placeholder.
    - get_entry(self): Entry - returns the Entry widget.
    - set_path(self, __path: str, only_existing: bool = True): None if only_existing is True and path is not exist this path won't be pasted.

    Notes:
    - This widget includes Entry and PushButton to specify the path to your file or directory
    """

    def __init__(
            self, 
            placed: Optional[str] = None, 
            placeholder: Optional[str] = None,
            size: tuple[int, int] = (200, 30), 
            font: Optional["QFont"] = None, 
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        self.setObjectName("path-entry")
        if font is not None: self.setFont(font)

        self.setStyleSheet(StyleSheetLoader.load_stylesheet(
            __file__, "styles/path_entry.css", 
            name="PathEntry", obj_name="QLineEdit#path-entry",
            stylesheet=stylesheet
        ))

        self.mainLayout = QHBoxLayout()

        self.pathEntry = Entry(placed, placeholder, size)

        self.specifyPathBtn = PushButton("...")
        self.specifyPathBtn.clicked.connect(lambda: self.set_path(FileDialog.get_open_file_name()))

        self.mainLayout.addWidget(self.pathEntry)
        self.mainLayout.addWidget(self.specifyPathBtn)
        self.mainLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.setLayout(self.mainLayout)

    def set_path(self, __path: Optional[str] = None, only_existing: bool = True) -> None:
        if __path is None: return

        if only_existing and os.path.exists(__path):
            self.pathEntry.setText(__path)
            return

        self.pathEntry.setText(__path)

    def get_entry(self) -> Entry:
        return self.pathEntry
    
