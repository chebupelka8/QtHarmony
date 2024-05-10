from PySide6.QtWidgets import QApplication

from typing import Optional


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
            raise ValueError("Intialize application use: 'Initialization.init()'")
