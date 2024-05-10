class FontNotFoundError(FileNotFoundError):
    ...

class FontExistsError(FileExistsError):
    ...

class NotInitializedError(RuntimeError):
    ...
