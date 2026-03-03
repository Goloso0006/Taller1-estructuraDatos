"""Estructura de datos tipo pila para carga de camión."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Paquete:
    """Representa un paquete cargado en el camión."""

    codigo: str
    destino: str


class PilaCamion:
    """Pila LIFO para optimizar carga y descarga de ruta."""

    def __init__(self) -> None:
        self._items: List[Paquete] = []

    def esta_vacia(self) -> bool:
        return len(self._items) == 0

    def apilar(self, paquete: Paquete) -> None:
        self._items.append(paquete)

    def desapilar(self) -> Optional[Paquete]:
        if self.esta_vacia():
            return None
        return self._items.pop()

    def cima(self) -> Optional[Paquete]:
        if self.esta_vacia():
            return None
        return self._items[-1]

    def listar(self) -> List[Paquete]:
        return list(self._items)
