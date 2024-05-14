import os
import json

from qtharmony.config import THEME_RESOURCES
from qtharmony.core import Loader

from .theme_builder import ThemeBuilder

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class ThemeManager:
    __widgets: list["QWidget"] = []
    __current_theme: str = os.path.join(THEME_RESOURCES, "dark-default.json") 

    @classmethod
    def change_theme(cls, __name: str) -> None:
        cls.__current_theme = cls.get_theme_by_name(__name)
        cls.update()

    @staticmethod
    def get_all_themes() -> dict[str, str]:
        res: dict[str, str] = {}

        for theme in os.listdir(THEME_RESOURCES):
            path = os.path.join(THEME_RESOURCES, theme)
            data = Loader.load_json(path)
            res[data["Info"]["name"]] = path
        
        return res
    
    @classmethod
    def get_theme_by_name(cls, __name: str) -> str:
        data = cls.get_all_themes()

        for theme in data.keys():
            try:
                if theme == __name:
                    return data[theme]
            
            except json.decoder.JSONDecodeError:
                ...
        
        raise FileExistsError(f"There is no such theme: {__name}")

    @classmethod
    def load_theme(cls, __path: str) -> None:
        cls.__current_theme = __path
    
    @classmethod
    def update(cls) -> None:
        data = ThemeBuilder.build_theme(cls.__current_theme)

        for widget in cls.__widgets:
            try:
                if hasattr(widget, "stylesheet"):
                    widget.setStyleSheet(data[widget.__class__.__name__] + widget.stylesheet)  # type: ignore
                
                else:
                    widget.setStyleSheet(data[widget.__class__.__name__])
            
            except KeyError:
                if hasattr(widget, "stylesheet"):
                    widget.setStyleSheet(widget.stylesheet)  # type: ignore

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
