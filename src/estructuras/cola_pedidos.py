"""Queue data structure for customer orders."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Order:
    """Represents one customer order."""

    code: str
    customer: str
    category: str


class OrderQueue:
    """FIFO queue for incoming orders."""

    def __init__(self) -> None:
        self._items: List[Order] = []

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def enqueue(self, order: Order) -> None:
        self._items.append(order)

    def dequeue(self) -> Optional[Order]:
        if self.is_empty():
            return None
        return self._items.pop(0)

    def front(self) -> Optional[Order]:
        if self.is_empty():
            return None
        return self._items[0]

    def list_items(self) -> List[Order]:
        return list(self._items)
