# Taller 1 - Estructura de Datos

## Esquema del proyecto

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

## Requerimientos implementados

- **Colas (FIFO):** recepción de pedidos por orden de llegada.
- **Pilas (LIFO):** gestión de carga/descarga de camión.
- **Arrays (fijo):** inventario de estanterías por posición física.
- **Frontend:** interfaz gráfica en Tkinter.
- **Paradigma:** diseño orientado a objetos (POO).

## Ejecución

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

## Arquitectura POO (resumen)

- `LogisticaService` coordina las operaciones de dominio.
- `ColaPedidos`, `PilaCamion` e `InventarioArray` encapsulan cada estructura.
- `LogisticaWindow` implementa la interfaz y delega acciones al servicio.
