from ..load import Loader

from qtharmony.src.config import THEME_RESOURCES
from typing import Optional


class ThemeBuilder:
    def __init__(self, __path: str) -> None:
        print(self.__to_css(Loader.load_theme(__path)))
    
    @classmethod
    def __to_css(cls, theme: dict) -> str:
        stylesheet_elements: list[str] = []

        for widget in theme.keys():
            object_name = theme[widget]["object-name"]

            for attr in theme[widget].keys():
                if attr == "object-name": continue

                stylesheet_elements.append(cls.__get_features_of_element(
                    theme[widget][attr], object_name, attr
                ))
        
        return "\n".join(stylesheet_elements)

    @classmethod
    def __get_features_of_element(cls, element: dict, object_name: str, pseudo_classes: Optional[str]) -> str:
        features = []

        for feature in element.keys():
            features.append(f"{feature}: {element[feature]};")
        
        if pseudo_classes is not None:
            object_name += pseudo_classes
        
        return (
            object_name + "{" +
            " ".join(features) +
            "}"
        )
