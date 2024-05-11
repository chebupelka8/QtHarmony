import os


class Loader:
    
    @staticmethod
    def load_file(__path: str) -> str:
        if not os.path.exists(__path):
            raise FileExistsError(f"No such file exists: {__path}")

        with open(__path, "r", encoding="utf-8") as outfile:
            result = outfile.read()
        
        return result
