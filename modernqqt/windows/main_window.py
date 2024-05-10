from PySide6.QtWidgets import QMainWindow, QWidget, QApplication

from modernqqt.src.core import Loader, StyleSheetLoader

from typing import Optional
import os.path


class MainWindow(QMainWindow):
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
        super().__init__(parent)

        if widget is not None: self.setCentralWidget(widget)
        
        self.setObjectName("main-window")
        self.setStyleSheet(StyleSheetLoader.load_stylesheet(
            __file__, "styles/main_window.css", 
            name="MainWindow", obj_name="QMainWindow#main-window",
            stylesheet=stylesheet
        ))

        self.resize(*size)
        if title is not None: self.setWindowTitle(title)
        else: self.setWindowTitle("ModernQQt")

        if not is_resizable: self.setFixedSize(*size)
    
    def run(self) -> None:
        self.show()
