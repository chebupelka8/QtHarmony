from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtGui import QIcon

from qtharmony.core import StyleSheetLoader
from qtharmony.config import UI_RESOURCES
from qtharmony.core.theme import ThemeManager

from typing import Optional
import os.path


class MainWindow(QMainWindow):
    """
    Custom QMainWindow widget for main window functionality.

    Methods:
    - __init__(widget: Optional[QWidget] = None, size: tuple[int, int] = (1000, 600),
              title: Optional[str] = None, is_resizable: bool = True,
              *, stylesheet: Optional[str] = None, parent: Optional[QWidget] = None): None
              - Initializes the MainWindow widget with optional central widget, size, title, resizable option, and stylesheet.
    
    - run(): None
              - Displays the main window.

    """

    def __init__(
            self, 
            widget: Optional[QWidget] = None,
            size: tuple[int, int] = (1000, 600),
            title: Optional[str] = None,
            is_resizable: bool = True,
            *,
            stylesheet: Optional[str] = None,
            parent: Optional[QWidget] = None
    ) -> None:
        """
        Initializes the MainWindow widget with optional central widget, size, title, resizable option, and stylesheet.

        Args:
            widget (Optional[QWidget], optional): The central widget to set in the main window. Defaults to None.
            size (tuple[int, int], optional): The size of the main window (width, height). Defaults to (1000, 600).
            title (Optional[str], optional): The title of the main window. Defaults to None.
            is_resizable (bool, optional): Flag to set if the main window is resizable. Defaults to True.
            stylesheet (Optional[str], optional): Custom stylesheet for the main window. Defaults to None.
            parent (Optional[QWidget], optional): Parent widget of the main window. Defaults to None.
        """ 

        super().__init__(parent)
        ThemeManager.add_widgets(self)

        if widget is not None: self.setCentralWidget(widget)
        self.setWindowIcon(QIcon(f"{os.path.join(UI_RESOURCES, 'Icon.png')}"))
        
        self.setObjectName("main-window")
        self.stylesheet = StyleSheetLoader.load_stylesheet(
            __file__, "styles/main_window.css", 
            name="MainWindow", obj_name="QMainWindow#main-window",
            stylesheet=stylesheet
        )

        self.resize(*size)
        if title is not None: self.setWindowTitle(title)
        else: self.setWindowTitle("QtHarmony")

        if not is_resizable: self.setFixedSize(*size)
    
    def run(self) -> None:
        self.show()
