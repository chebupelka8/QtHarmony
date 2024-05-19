from PySide6.QtWidgets import QSplitter
from PySide6.QtCore import Qt

from qtharmony.core import StyleSheetLoader
from qtharmony.core.theme import ThemeManager
from qtharmony.core.sizes import AbstractSize

from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class Splitter(QSplitter):
    """
    Custom QSplitter widget for managing layout splitting.

    Methods:
    - __init__(__orientation: str, *, parent=None): None - Initializes the splitter with a specified orientation.
    - addWidget(widget): None - Adds a widget to the splitter and sets it as non-collapsible.
    """

    def __init__(
            self, 
            __orientation: str,
            size: Optional[AbstractSize] = None,
            is_active: bool = True,
            *,
            object_name: str = "splitter",
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        """
        Initializes the Splitter instance with the specified orientation.

        Args:
            __orientation (str): The orientation of the splitter, either "horizontal" or "vertical".
            stylesheet (Optional[str], optional): Custom stylesheet for the splitter. Defaults to None.
            parent (Optional["QWidget"], optional): Parent widget of the splitter. Defaults to None.
        """

        if __orientation == "horizontal": super().__init__(Qt.Orientation.Horizontal, parent)
        elif __orientation == "vertical": super().__init__(Qt.Orientation.Vertical, parent)

        ThemeManager.add_widgets(self)

        self.setDisabled(not is_active)
        if size is not None: size.use(self)

        self.setObjectName(object_name)
        self.stylesheet = StyleSheetLoader.load_stylesheet(
            __file__, "styles/splitter.css", 
            name=self.__class__.__name__, obj_name=f"QSplitter#{self.objectName()}",
            stylesheet=stylesheet
        )

    def addWidget(self, widget, stretch: Optional[int] = None):
        """
        Adds a widget to the splitter and sets it as non-collapsible.

        Args:
            widget (QWidget): The widget to be added to the splitter.
        """

        super().addWidget(widget)
        index = self.indexOf(widget)

        if stretch is not None: self.setStretchFactor(index, stretch)
        self.setCollapsible(index, False)

