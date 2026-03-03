"""Ventana principal Tkinter para gestionar estructuras de datos."""

import tkinter as tk
from tkinter import messagebox, ttk

from src.servicios.logistica_service import LogisticaService


class LogisticaWindow(tk.Tk):
    """Interfaz gráfica principal para el taller."""

    def __init__(self, service: LogisticaService) -> None:
        super().__init__()
        self._service = service
        self.title("Taller 1 - Estructuras de Datos")
        self.geometry("860x600")
        self.resizable(True, True)

        self._build_ui()
        self._refresh_all()

    def _build_ui(self) -> None:
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self._tab_cola = ttk.Frame(notebook)
        self._tab_pila = ttk.Frame(notebook)
        self._tab_array = ttk.Frame(notebook)

        notebook.add(self._tab_cola, text="Cola de pedidos")
        notebook.add(self._tab_pila, text="Pila de camión")
        notebook.add(self._tab_array, text="Array inventario")

        self._build_tab_cola()
        self._build_tab_pila()
        self._build_tab_array()

    def _build_tab_cola(self) -> None:
        form = ttk.LabelFrame(self._tab_cola, text="Registrar pedido")
        form.pack(fill="x", padx=10, pady=10)

        ttk.Label(form, text="Código").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        ttk.Label(form, text="Cliente").grid(row=0, column=2, padx=6, pady=6, sticky="w")
        ttk.Label(form, text="Categoría").grid(row=0, column=4, padx=6, pady=6, sticky="w")

        self._pedido_codigo = tk.StringVar()
        self._pedido_cliente = tk.StringVar()
        self._pedido_categoria = tk.StringVar()

        ttk.Entry(form, textvariable=self._pedido_codigo, width=18).grid(row=0, column=1, padx=6, pady=6)
        ttk.Entry(form, textvariable=self._pedido_cliente, width=20).grid(row=0, column=3, padx=6, pady=6)
        ttk.Entry(form, textvariable=self._pedido_categoria, width=20).grid(row=0, column=5, padx=6, pady=6)

        ttk.Button(form, text="Encolar", command=self._on_encolar_pedido).grid(row=0, column=6, padx=6, pady=6)
        ttk.Button(form, text="Atender", command=self._on_atender_pedido).grid(row=0, column=7, padx=6, pady=6)

        self._cola_list = tk.Listbox(self._tab_cola, height=18)
        self._cola_list.pack(fill="both", expand=True, padx=10, pady=10)

    def _build_tab_pila(self) -> None:
        form = ttk.LabelFrame(self._tab_pila, text="Gestión de carga")
        form.pack(fill="x", padx=10, pady=10)

        ttk.Label(form, text="Código paquete").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        ttk.Label(form, text="Destino").grid(row=0, column=2, padx=6, pady=6, sticky="w")

        self._paq_codigo = tk.StringVar()
        self._paq_destino = tk.StringVar()

        ttk.Entry(form, textvariable=self._paq_codigo, width=18).grid(row=0, column=1, padx=6, pady=6)
        ttk.Entry(form, textvariable=self._paq_destino, width=20).grid(row=0, column=3, padx=6, pady=6)

        ttk.Button(form, text="Apilar", command=self._on_apilar_paquete).grid(row=0, column=4, padx=6, pady=6)
        ttk.Button(form, text="Desapilar", command=self._on_desapilar_paquete).grid(row=0, column=5, padx=6, pady=6)

        self._pila_list = tk.Listbox(self._tab_pila, height=18)
        self._pila_list.pack(fill="both", expand=True, padx=10, pady=10)

    def _build_tab_array(self) -> None:
        form = ttk.LabelFrame(self._tab_array, text="Asignar inventario")
        form.pack(fill="x", padx=10, pady=10)

        ttk.Label(form, text="Índice (0..n-1)").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        ttk.Label(form, text="Categoría").grid(row=0, column=2, padx=6, pady=6, sticky="w")
        ttk.Label(form, text="Producto").grid(row=0, column=4, padx=6, pady=6, sticky="w")

        self._inv_indice = tk.StringVar()
        self._inv_categoria = tk.StringVar()
        self._inv_producto = tk.StringVar()

        ttk.Entry(form, textvariable=self._inv_indice, width=15).grid(row=0, column=1, padx=6, pady=6)
        ttk.Entry(form, textvariable=self._inv_categoria, width=18).grid(row=0, column=3, padx=6, pady=6)
        ttk.Entry(form, textvariable=self._inv_producto, width=18).grid(row=0, column=5, padx=6, pady=6)

        ttk.Button(form, text="Asignar", command=self._on_asignar_inventario).grid(row=0, column=6, padx=6, pady=6)

        self._array_list = tk.Listbox(self._tab_array, height=18)
        self._array_list.pack(fill="both", expand=True, padx=10, pady=10)

    def _on_encolar_pedido(self) -> None:
        codigo = self._pedido_codigo.get().strip()
        cliente = self._pedido_cliente.get().strip()
        categoria = self._pedido_categoria.get().strip()

        if not codigo or not cliente or not categoria:
            messagebox.showwarning("Datos incompletos", "Completa código, cliente y categoría.")
            return

        self._service.registrar_pedido(codigo=codigo, cliente=cliente, categoria=categoria)
        self._pedido_codigo.set("")
        self._pedido_cliente.set("")
        self._pedido_categoria.set("")
        self._refresh_cola()

    def _on_atender_pedido(self) -> None:
        pedido = self._service.atender_pedido()
        if pedido is None:
            messagebox.showinfo("Cola vacía", "No hay pedidos para atender.")
            return

        messagebox.showinfo("Pedido atendido", f"Se atendió: {pedido.codigo} - {pedido.cliente}")
        self._refresh_cola()

    def _on_apilar_paquete(self) -> None:
        codigo = self._paq_codigo.get().strip()
        destino = self._paq_destino.get().strip()

        if not codigo or not destino:
            messagebox.showwarning("Datos incompletos", "Completa código y destino.")
            return

        self._service.cargar_paquete(codigo=codigo, destino=destino)
        self._paq_codigo.set("")
        self._paq_destino.set("")
        self._refresh_pila()

    def _on_desapilar_paquete(self) -> None:
        paquete = self._service.descargar_paquete()
        if paquete is None:
            messagebox.showinfo("Pila vacía", "No hay paquetes para descargar.")
            return

        messagebox.showinfo("Paquete descargado", f"Se descargó: {paquete.codigo} ({paquete.destino})")
        self._refresh_pila()

    def _on_asignar_inventario(self) -> None:
        indice_txt = self._inv_indice.get().strip()
        categoria = self._inv_categoria.get().strip()
        producto = self._inv_producto.get().strip()

        if not indice_txt or not categoria or not producto:
            messagebox.showwarning("Datos incompletos", "Completa índice, categoría y producto.")
            return

        try:
            indice = int(indice_txt)
            self._service.asignar_inventario(indice=indice, categoria=categoria, producto=producto)
        except ValueError:
            messagebox.showerror("Índice inválido", "El índice debe ser numérico.")
            return
        except IndexError as exc:
            messagebox.showerror("Fuera de rango", str(exc))
            return

        self._inv_indice.set("")
        self._inv_categoria.set("")
        self._inv_producto.set("")
        self._refresh_array()

    def _refresh_all(self) -> None:
        self._refresh_cola()
        self._refresh_pila()
        self._refresh_array()

    def _refresh_cola(self) -> None:
        self._cola_list.delete(0, tk.END)
        for i, pedido in enumerate(self._service.listar_pedidos(), start=1):
            item = f"{i}. [{pedido.codigo}] {pedido.cliente} - {pedido.categoria}"
            self._cola_list.insert(tk.END, item)

    def _refresh_pila(self) -> None:
        self._pila_list.delete(0, tk.END)
        carga = self._service.listar_carga()
        for pos, paquete in enumerate(reversed(carga), start=1):
            item = f"{pos}. [{paquete.codigo}] {paquete.destino}"
            self._pila_list.insert(tk.END, item)

    def _refresh_array(self) -> None:
        self._array_list.delete(0, tk.END)
        for indice, slot in enumerate(self._service.obtener_inventario()):
            if slot is None:
                item = f"{indice}: (vacío)"
            else:
                item = f"{indice}: {slot.categoria} -> {slot.producto}"
            self._array_list.insert(tk.END, item)
