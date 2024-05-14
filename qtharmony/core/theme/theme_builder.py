from ..load import Loader

from qtharmony.config import THEME_RESOURCES
from typing import Optional

import json


class ThemeBuilder:

    @classmethod
    def build_theme(cls, __path: str) -> dict:
        return cls.__to_css(Loader.load_theme(__path))
    
    @classmethod
    def __to_css(cls, theme: dict) -> dict: 
        result = {}

        for widget in theme.keys():
            stylesheet_elements: list[str] = []
            object_name = theme[widget]["object-name"]

            for attr in theme[widget].keys():
                if attr == "object-name": continue

                stylesheet_elements.append(cls.__get_features_of_element(
                    theme[widget][attr], object_name, attr
                ))
            
            result[widget] = "\n".join(stylesheet_elements) + "\n"
        
        return result

    @staticmethod
    def __get_features_of_element(element: dict, object_name: str, pseudo_class: Optional[str]) -> str:
        features = []

        for feature in element.keys():
            features.append(f"{feature}: {element[feature]};")
        
        if pseudo_class is not None:
            object_name += pseudo_class
        
        return (
            object_name + "{" +
            " ".join(features) +
            "}"
        )
