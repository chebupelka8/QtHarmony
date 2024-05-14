from qtharmony.widgets import Frame
from qtharmony.src.core.theme import ThemeManager


class TextBox(Frame):
    def __init__(self) -> None:
        super().__init__(object_name="text-frame", stylesheet="TextBox {background-color: green}")
        ThemeManager.add_widgets(self)

