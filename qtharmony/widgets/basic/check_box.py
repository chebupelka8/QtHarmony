from PySide6.QtWidgets import QCheckBox
from PySide6.QtCore import QSize

from qtharmony.src.core import StyleSheetLoader

from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class CheckBox(QCheckBox):
    def __init__(
            self,
            text: Optional[str] = None,
            size: tuple[int, int] = (150, 30),
            is_checkable: bool = True,
            is_checked: bool = False,
            is_disabled: bool = False,
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        self.setFixedSize(QSize(*size))
        self.setChecked(is_checked)
        self.setCheckable(is_checkable)
        self.setDisabled(is_disabled)

        self.setObjectName("check-box")
        if text is not None:
            self.setText(text)
        
        self.setStyleSheet(StyleSheetLoader.load_stylesheet(
            __file__, "styles/check_box.css", 
            name="CheckBox", obj_name="CheckBox#check-box",
            stylesheet=stylesheet
        ))

