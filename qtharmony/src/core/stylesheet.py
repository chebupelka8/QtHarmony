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
