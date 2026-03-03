"""Stack data structure for truck loading."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Package:
    """Represents one loaded package."""

    code: str
    destination: str


class TruckStack:
    """LIFO stack for truck load and unload."""

    def __init__(self) -> None:
        self._items: List[Package] = []

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def push(self, package: Package) -> None:
        self._items.append(package)

    def pop(self) -> Optional[Package]:
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self) -> Optional[Package]:
        if self.is_empty():
            return None
        return self._items[-1]

    def list_items(self) -> List[Package]:
        return list(self._items)
