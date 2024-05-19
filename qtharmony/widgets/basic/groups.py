from typing import Optional, TYPE_CHECKING
from PySide6.QtWidgets import (
    QGroupBox, QHBoxLayout, QVBoxLayout
)

from qtharmony.core import StyleSheetLoader
from qtharmony.core.theme import ThemeManager 
from qtharmony.core.sizes import AbstractSize

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


def copy_method(source_class, method_name):
    
    def decorator(target_class):
    
        def wrapper(self, *args, **kwargs):
            source_method = getattr(source_class, method_name)
            return source_method(self, *args, **kwargs)
    
        setattr(target_class, method_name, wrapper)
        return target_class
    
    return decorator


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
            size: Optional[AbstractSize] = None,
            orientation: str = "vertical",
            is_active: bool = True,
            *,
            object_name: str = "group-box",
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
        ThemeManager.add_widgets(self)

        self.setObjectName(object_name)
        self.stylesheet = StyleSheetLoader.load_stylesheet(
            __file__, "styles/group_box.css", 
            name=self.__class__.__name__, obj_name=f"QGroupBox#{self.objectName()}",
            stylesheet=stylesheet
        )

        if title is not None: self.setTitle(title)
        if size is not None: size.use(self)

        if orientation == "vertical": self.mainLayout = QVBoxLayout()
        elif orientation == "horizontal": self.mainLayout = QHBoxLayout()
        else: raise ValueError("Invalid orientation. should be use 'vertical' or 'horizontal'.")

        self.setDisabled(not is_active)

        self.setLayout(self.mainLayout)
    
    def addWidget(self, *args, **kwargs) -> None:
        self.mainLayout.addWidget(*args, **kwargs)
    
    def addLayout(self, *args, **kwargs) -> None:
        self.mainLayout.addLayout(*args, **kwargs)
    
    def addItem(self, *args, **kwargs) -> None:
        self.mainLayout.addItem(*args, **kwargs)
