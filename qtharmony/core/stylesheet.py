from .load import Loader

import os.path
from typing import Optional


class StyleSheetLoader:
    
    @staticmethod
    def load_stylesheet(
        __file: str, __path: str, 
        name: str, obj_name: str,
        stylesheet: Optional[str] = None,
    ) -> str:
        stylesheet_path = os.path.join(os.path.dirname(__file), __path)

        if stylesheet is not None:
            return (
                Loader.load_file(stylesheet_path) + "\n" 
                + stylesheet.replace(name, obj_name)
            )
        else:
            return Loader.load_file(stylesheet_path)
    
    @staticmethod
    def append_stylesheet(
        default_stylesheet: Optional[str],
        additional: str,
        name: str, obj_name: str,
        reversed: bool = False
    ) -> str:
        
        result = ""

        if not reversed:
            if default_stylesheet is not None:
                result = default_stylesheet + "\n"

            result += "\n" + additional.replace(name, obj_name) + "\n"
        
        else:
            result = additional.replace(name, obj_name) + "\n"

            if default_stylesheet is not None:
                result += "\n" + default_stylesheet + "\n"
        
        return result
