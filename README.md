# Workshop 1 - Data Structures

## Project layout

```
Taller1/
├── main.py
├── README.md
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── ui/
│   │   ├── __init__.py
│   │   └── app_window.py
│   ├── estructuras/
│   │   ├── __init__.py
│   │   ├── cola_pedidos.py
│   │   ├── pila_camion.py
│   │   └── inventario_array.py
│   ├── servicios/
│   │   ├── __init__.py
│   │   └── logistica_service.py
│   └── utils/
│       └── __init__.py
└── tests/
    └── __init__.py
```

## Implemented requirements

- **Queues (FIFO):** receive customer orders in arrival order.
- **Stacks (LIFO):** manage truck load and unload.
- **Fixed arrays:** inventory by physical shelf position.
- **Frontend:** graphical interface in Tkinter.
- **Paradigm:** object-oriented programming (OOP).

## Run

From the project root folder:

```
python main.py
```

## OOP architecture (summary)

- `LogisticsService` coordinates domain operations.
- `OrderQueue`, `TruckStack`, and `InventoryArray` encapsulate each structure.
- `LogisticsWindow` implements the UI and delegates actions to the service.
