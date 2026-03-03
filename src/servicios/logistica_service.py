"Domain service to coordinate orders, load, and inventory."

from typing import List, Optional

from src.estructuras.cola_pedidos import Order, OrderQueue
from src.estructuras.inventario_array import InventoryArray, InventorySlot
from src.estructuras.pila_camion import Package, TruckStack


class LogisticsService:
    "Business facade using object-oriented design."

    def __init__(self, inventory_capacity: int = 10) -> None:
        self._order_queue = OrderQueue()
        self._truck_stack = TruckStack()
        self._inventory = InventoryArray(capacity=inventory_capacity)

    def register_order(self, code: str, customer: str, category: str) -> Order:
        order = Order(code=code, customer=customer, category=category)
        self._order_queue.enqueue(order)
        return order

    def serve_order(self) -> Optional[Order]:
        return self._order_queue.dequeue()

    def list_orders(self) -> List[Order]:
        return self._order_queue.list_items()

    def load_package(self, code: str, destination: str) -> Package:
        package = Package(code=code, destination=destination)
        self._truck_stack.push(package)
        return package

    def unload_package(self) -> Optional[Package]:
        return self._truck_stack.pop()

    def list_load(self) -> List[Package]:
        return self._truck_stack.list_items()

    def assign_inventory(self, index: int, category: str, product: str) -> None:
        self._inventory.assign(index=index, category=category, product=product)

    def get_inventory(self) -> List[Optional[InventorySlot]]:
        return self._inventory.list_items()

    @property
    def inventory_capacity(self) -> int:
        return self._inventory.capacity
