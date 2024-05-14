from PySide6.QtWidgets import QApplication

from typing import Optional
from qtharmony.core.exceptions import NotInitializedError
from qtharmony.core.theme import ThemeManager


class Initialization:

    application: Optional[QApplication] = None

    @classmethod
    def init(cls, argv: list[str]) -> None:
        cls.application = QApplication(argv)
    
    @classmethod
    def exec(cls) -> None:
        if cls.application is not None:
            ThemeManager.update()
            cls.application.exec()
        
        else:
            raise NotInitializedError("Intialize application use: 'Initialization.init()'")
