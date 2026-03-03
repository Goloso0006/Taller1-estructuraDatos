"""Array de tamaño fijo para inventario de estanterías."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class SlotInventario:
    """Representa una posición física del inventario."""

    indice: int
    categoria: str
    producto: str


class InventarioArray:
    """Arreglo fijo que modela pasillos/estanterías por índice."""

    def __init__(self, capacidad: int) -> None:
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que cero.")
        self._capacidad = capacidad
        self._items: List[Optional[SlotInventario]] = [None] * capacidad

    @property
    def capacidad(self) -> int:
        return self._capacidad

    def asignar(self, indice: int, categoria: str, producto: str) -> None:
        self._validar_indice(indice)
        self._items[indice] = SlotInventario(indice=indice, categoria=categoria, producto=producto)

    def obtener(self, indice: int) -> Optional[SlotInventario]:
        self._validar_indice(indice)
        return self._items[indice]

    def listar(self) -> List[Optional[SlotInventario]]:
        return list(self._items)

    def _validar_indice(self, indice: int) -> None:
        if indice < 0 or indice >= self._capacidad:
            raise IndexError(f"Índice fuera de rango: {indice}. Rango válido: 0 a {self._capacidad - 1}.")
