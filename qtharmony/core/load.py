import os

import json


class Loader:

    @staticmethod
    def __verify_exists(__path: str) -> None:
        if not os.path.exists(__path):
            raise FileExistsError(f"No such file exists: {__path}")
    
    @classmethod
    def load_file(cls, __path: str) -> str:
        cls.__verify_exists(__path)

        with open(__path, "r", encoding="utf-8") as outfile:
            result = outfile.read()
        
        return result

    @classmethod
    def load_json(cls, __path: str) -> dict:
        cls.__verify_exists(__path)

        with open(__path, "r", encoding="utf-8") as outfile:
            result = json.load(outfile)
        
        return result
    
    @classmethod
    def load_theme(cls, __path: str) -> dict:
        cls.__verify_exists(__path)

        result = cls.load_json(__path)
        
        del result["Info"]
        return result
