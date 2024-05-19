from typing import TYPE_CHECKING, Optional

from dataclasses import dataclass
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


@dataclass
class Size:
    width: Optional[int]
    height: Optional[int]

    def ratio(self) -> str:
        if len(self.valid_size()) == 2: 
            return "Size"
        else:
            return [i for i in ("width", "height") 
                    if not i.startswith("_") and getattr(self, i) is not None][0].capitalize()

    def valid_size(self) -> tuple[int]:
        return tuple(filter(
            lambda x: isinstance(x, int), (self.width, self.height)
        ))  # type: ignore


class AbstractSize(ABC):
    
    @abstractmethod
    def use(self, widget: "QWidget") -> None:
        ...


class SizeBuilder(AbstractSize):
    def __init__(self, width: Optional[int], height: Optional[int], method) -> None:
        self.size: Size = Size(width, height)
        self.method = method

    def use(self, widget: "QWidget") -> None:
        method = f"{self.method}{self.size.ratio()}"

        if hasattr(widget, method):
            getattr(widget, method)(*self.size.valid_size())
        
        else:
            raise ValueError("Invalid widget type.")


class SizeGroup(AbstractSize):
    def __init__(self, *sizes) -> None:
        self.sizes: list[AbstractSize] = [*sizes]
    
    def use(self, widget: "QWidget") -> None:
        for size in self.sizes:
            size.use(widget)


class FixedSize(SizeBuilder):
    def __init__(self, width: Optional[int] = None, height: Optional[int] = None) -> None:
        super().__init__(width, height, "setFixed")


class MaximalSize(SizeBuilder):
    def __init__(self, width: Optional[int] = None, height: Optional[int] = None) -> None:
        super().__init__(width, height, "setMaximum")


class MinimalSize(SizeBuilder):
    def __init__(self, width: Optional[int] = None, height: Optional[int] = None) -> None:
        super().__init__(width, height, "setMinimum")
