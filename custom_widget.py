from PySide6.QtWidgets import QPlainTextEdit

from qtharmony.src.core.theme import ThemeManager


class TextBox(QPlainTextEdit):
    def __init__(self) -> None:
        super().__init__()
        ThemeManager.add_widgets(self)

        self.setObjectName("text-box")
