"""Estructura de datos tipo cola para recepción de pedidos."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Pedido:
    """Representa un pedido ingresado por un cliente."""

    codigo: str
    cliente: str
    categoria: str


class ColaPedidos:
    """Cola FIFO para pedidos en orden de llegada."""

    def __init__(self) -> None:
        self._items: List[Pedido] = []

    def esta_vacia(self) -> bool:
        return len(self._items) == 0

    def encolar(self, pedido: Pedido) -> None:
        self._items.append(pedido)

    def desencolar(self) -> Optional[Pedido]:
        if self.esta_vacia():
            return None
        return self._items.pop(0)

    def frente(self) -> Optional[Pedido]:
        if self.esta_vacia():
            return None
        return self._items[0]

    def listar(self) -> List[Pedido]:
        return list(self._items)
