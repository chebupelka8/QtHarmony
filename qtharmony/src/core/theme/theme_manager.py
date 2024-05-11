import os
import json

from qtharmony.src.config import THEME_RESOURCES
from qtharmony.src.core import Loader

from .theme_builder import ThemeBuilder

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class ThemeManager:
    __widgets: list["QWidget"] = []
    __current_theme: str = "Dark-Default" 

    @staticmethod
    def get_all_themes() -> list[str]:
        res: list[str] = []

        for theme in os.listdir(THEME_RESOURCES):
            res.append(os.path.join(THEME_RESOURCES, theme))
        
        return res
    
    @classmethod
    def get_theme_by_name(cls, __name: str) -> str:
        for theme in cls.get_all_themes():
            try:
                if Loader.load_json(theme)["Info"]["name"] == __name:
                    return theme
            
            except json.decoder.JSONDecodeError:
                ...
        
        raise FileExistsError(f"There is no such theme: {__name}")
    
    @classmethod
    def update(cls) -> None:
        data = ThemeBuilder.build_theme(cls.get_theme_by_name(cls.__current_theme))

        for widget in cls.__widgets:
            widget.setStyleSheet(data[widget.__class__.__name__] + widget.styleSheet())
            
            # print(widget.styleSheet())
            # print("\n\n\n----------------\n\n\n")
            # print(widget.styleSheet())

            # print(data[widget.__class__.__name__])

    @classmethod
    def add_widgets(cls, *__widgets: "QWidget") -> None:
        for widget in __widgets:
            cls.__widgets.append(widget)
    
    @classmethod
    def remove_widgets(cls, *__widgets: "QWidget") -> None:
        for widget in __widgets:
            cls.__widgets.remove(widget)
    
    @classmethod
    def get_widgets(cls) -> list["QWidget"]:
        return cls.__widgets
