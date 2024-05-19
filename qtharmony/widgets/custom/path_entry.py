import os.path

from PySide6.QtWidgets import ( 
    QWidget, QHBoxLayout, 
    QSpacerItem, QSizePolicy
)

from qtharmony.core import FileDialog, StyleSheetLoader
from qtharmony.core.sizes import AbstractSize, FixedSize

from ..basic.button import PushButton
from ..basic.entry import Entry

from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from PySide6.QtGui import QFont


class PathEntry(QWidget):
    """
    Custom QWidget combining a QLineEdit for path input and a button to specify the path.

    Methods:
    - __init__(placed: Optional[str] = None, placeholder: Optional[str] = None, size: tuple[int, int] = (200, 30),
              font: Optional["QFont"] = None, *, stylesheet: Optional[str] = None, parent: Optional["QWidget"] = None): None
              - Initializes the PathEntry widget with path input functionality.
    - set_path(__path: Optional[str] = None, only_existing: bool = True) -> None
              - Sets the path in the path entry widget.
    - get_entry() -> Entry
              - Returns the Entry widget used for path input.
    """

    def __init__(
            self, 
            placed: Optional[str] = None, 
            placeholder: Optional[str] = None,
            size: Optional[AbstractSize] = None,
            font: Optional["QFont"] = None, 
            is_active: bool = True,
            *,
            object_name: str = "path-entry",
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        """
        Initializes the PathEntry widget with path input functionality.

        Args:
            placed (Optional[str], optional): The initial path text. Defaults to None.
            placeholder (Optional[str], optional): The placeholder text for the path entry. Defaults to None.
            size (tuple[int, int], optional): The size of the path entry widget (width, height). Defaults to (200, 30).
            font (Optional["QFont"], optional): The font to be used for text input. Defaults to None.
            stylesheet (Optional[str], optional): Custom stylesheet for the path entry widget. Defaults to None.
            parent (Optional["QWidget"], optional): Parent widget of the path entry. Defaults to None.
        """        

        super().__init__(parent)

        self.setObjectName(object_name)
        if font is not None: self.setFont(font)
        if size is not None: size.use(self)
        self.setDisabled(not is_active)

        self.setStyleSheet(StyleSheetLoader.load_stylesheet(
            __file__, "styles/path_entry.css", 
            name=self.__class__.__name__, obj_name=f"QWidget#{self.objectName()}",
            stylesheet=stylesheet
        ))

        print(self.styleSheet())

        self.mainLayout = QHBoxLayout()

        self.pathEntry = Entry(placed, placeholder, size)

        self.specifyPathBtn = PushButton("...", size=FixedSize(28, 28))
        self.specifyPathBtn.clicked.connect(lambda: self.set_path(FileDialog.get_open_file_name()))

        self.mainLayout.addWidget(self.pathEntry)
        self.mainLayout.addWidget(self.specifyPathBtn)
        self.mainLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.setLayout(self.mainLayout)

    def set_path(self, __path: Optional[str] = None, only_existing: bool = True) -> None:
        """
        Sets the path in the path entry widget.

        Args:
            __path (Optional[str], optional): The path to be set. Defaults to None.
            only_existing (bool, optional): Flag to only set the path if it exists. Defaults to True.
        """

        if __path is None: return

        if only_existing and os.path.exists(__path):
            self.pathEntry.setText(__path)
            return

        self.pathEntry.setText(__path)

    def get_entry(self) -> Entry:
        """
        Returns the Entry widget used for path input.

        Returns:
            Entry: The Entry widget for path input.
        """

        return self.pathEntry
    
