from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


def set_widget_size(widget: "QWidget", **kwargs: tuple[int, int]) -> None:
    match kwargs:
        case kw if "fixed_size" in kw:
            widget.setFixedSize(*kwargs["fixed_size"])
        
        case kw if "min_size" in kw:
            widget.setMinimumSize(*kwargs["min_size"])
        
        case kw if "max_size" in kw:
            widget.setMaximumSize(*kwargs["max_size"])
        
        case _:
            raise ValueError("Invalid combination of arguments.")
