from PySide6.QtWidgets import QApplication

from typing import Optional
from qtharmony.src.core.exceptions import NotInitializedError


class Initialization:

    application: Optional[QApplication] = None

    @classmethod
    def init(cls, argv: list[str]) -> None:
        cls.application = QApplication(argv)
    
    @classmethod
    def exec(cls) -> None:
        if cls.application is not None:
            cls.application.exec()
        
        else:
            raise NotInitializedError("Intialize application use: 'Initialization.init()'")
