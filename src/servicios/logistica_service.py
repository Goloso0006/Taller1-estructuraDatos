"""Servicio de dominio para coordinar pedidos, carga e inventario."""

from typing import List, Optional

from src.estructuras.cola_pedidos import ColaPedidos, Pedido
from src.estructuras.inventario_array import InventarioArray, SlotInventario
from src.estructuras.pila_camion import Paquete, PilaCamion


class LogisticaService:
    """Fachada de lógica de negocio bajo paradigma POO."""

    def __init__(self, capacidad_inventario: int = 10) -> None:
        self._cola_pedidos = ColaPedidos()
        self._pila_camion = PilaCamion()
        self._inventario = InventarioArray(capacidad=capacidad_inventario)

    def registrar_pedido(self, codigo: str, cliente: str, categoria: str) -> Pedido:
        pedido = Pedido(codigo=codigo, cliente=cliente, categoria=categoria)
        self._cola_pedidos.encolar(pedido)
        return pedido

    def atender_pedido(self) -> Optional[Pedido]:
        return self._cola_pedidos.desencolar()

    def listar_pedidos(self) -> List[Pedido]:
        return self._cola_pedidos.listar()

    def cargar_paquete(self, codigo: str, destino: str) -> Paquete:
        paquete = Paquete(codigo=codigo, destino=destino)
        self._pila_camion.apilar(paquete)
        return paquete

    def descargar_paquete(self) -> Optional[Paquete]:
        return self._pila_camion.desapilar()

    def listar_carga(self) -> List[Paquete]:
        return self._pila_camion.listar()

    def asignar_inventario(self, indice: int, categoria: str, producto: str) -> None:
        self._inventario.asignar(indice=indice, categoria=categoria, producto=producto)

    def obtener_inventario(self) -> List[Optional[SlotInventario]]:
        return self._inventario.listar()

    @property
    def capacidad_inventario(self) -> int:
        return self._inventario.capacidad
