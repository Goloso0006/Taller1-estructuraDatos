"""Fixed-size array for shelf inventory."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class InventorySlot:
    """Represents one physical inventory slot."""

    index: int
    category: str
    product: str


class InventoryArray:
    """Fixed array that models shelf positions by index."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self._capacity = capacity
        self._items: List[Optional[InventorySlot]] = [None] * capacity

    @property
    def capacity(self) -> int:
        return self._capacity

    def assign(self, index: int, category: str, product: str) -> None:
        self._validate_index(index)
        self._items[index] = InventorySlot(index=index, category=category, product=product)

    def get(self, index: int) -> Optional[InventorySlot]:
        self._validate_index(index)
        return self._items[index]

    def list_items(self) -> List[Optional[InventorySlot]]:
        return list(self._items)

    def _validate_index(self, index: int) -> None:
        if index < 0 or index >= self._capacity:
            raise IndexError(f"Index out of range: {index}. Valid range: 0 to {self._capacity - 1}.")
