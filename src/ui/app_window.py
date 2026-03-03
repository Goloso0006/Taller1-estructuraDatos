"Main Tkinter window to manage data structures."

import tkinter as tk
from tkinter import messagebox, ttk

from src.servicios.logistica_service import LogisticsService


class LogisticsWindow(tk.Tk):
    "Main graphical interface for the project." 

    def __init__(self, service: LogisticsService) -> None:
        super().__init__()
        self._service = service
        self.title("Workshop 1 - Data Structures")
        self.geometry("860x600")
        self.resizable(True, True)

        self._build_ui()
        self._refresh_all()

    def _build_ui(self) -> None:
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self._tab_queue = ttk.Frame(notebook)
        self._tab_stack = ttk.Frame(notebook)
        self._tab_array = ttk.Frame(notebook)

        notebook.add(self._tab_queue, text="Order Queue")
        notebook.add(self._tab_stack, text="Truck Stack")
        notebook.add(self._tab_array, text="Inventory Array")

        self._build_tab_queue()
        self._build_tab_stack()
        self._build_tab_array()

    def _build_tab_queue(self) -> None:
        form = ttk.LabelFrame(self._tab_queue, text="Register Order")
        form.pack(fill="x", padx=10, pady=10)

        ttk.Label(form, text="Code").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        ttk.Label(form, text="Customer").grid(row=0, column=2, padx=6, pady=6, sticky="w")
        ttk.Label(form, text="Category").grid(row=0, column=4, padx=6, pady=6, sticky="w")

        self._order_code = tk.StringVar()
        self._order_customer = tk.StringVar()
        self._order_category = tk.StringVar()

        ttk.Entry(form, textvariable=self._order_code, width=18).grid(row=0, column=1, padx=6, pady=6)
        ttk.Entry(form, textvariable=self._order_customer, width=20).grid(row=0, column=3, padx=6, pady=6)
        ttk.Entry(form, textvariable=self._order_category, width=20).grid(row=0, column=5, padx=6, pady=6)

        ttk.Button(form, text="Enqueue", command=self._on_enqueue_order).grid(row=0, column=6, padx=6, pady=6)
        ttk.Button(form, text="Serve", command=self._on_serve_order).grid(row=0, column=7, padx=6, pady=6)

        self._queue_list = tk.Listbox(self._tab_queue, height=18)
        self._queue_list.pack(fill="both", expand=True, padx=10, pady=10)

    def _build_tab_stack(self) -> None:
        form = ttk.LabelFrame(self._tab_stack, text="Load Management")
        form.pack(fill="x", padx=10, pady=10)

        ttk.Label(form, text="Package Code").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        ttk.Label(form, text="Destination").grid(row=0, column=2, padx=6, pady=6, sticky="w")

        self._package_code = tk.StringVar()
        self._package_destination = tk.StringVar()

        ttk.Entry(form, textvariable=self._package_code, width=18).grid(row=0, column=1, padx=6, pady=6)
        ttk.Entry(form, textvariable=self._package_destination, width=20).grid(row=0, column=3, padx=6, pady=6)

        ttk.Button(form, text="Push", command=self._on_push_package).grid(row=0, column=4, padx=6, pady=6)
        ttk.Button(form, text="Pop", command=self._on_pop_package).grid(row=0, column=5, padx=6, pady=6)

        self._stack_list = tk.Listbox(self._tab_stack, height=18)
        self._stack_list.pack(fill="both", expand=True, padx=10, pady=10)

    def _build_tab_array(self) -> None:
        form = ttk.LabelFrame(self._tab_array, text="Assign Inventory")
        form.pack(fill="x", padx=10, pady=10)

        ttk.Label(form, text="Index (0..n-1)").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        ttk.Label(form, text="Category").grid(row=0, column=2, padx=6, pady=6, sticky="w")
        ttk.Label(form, text="Product").grid(row=0, column=4, padx=6, pady=6, sticky="w")

        self._inventory_index = tk.StringVar()
        self._inventory_category = tk.StringVar()
        self._inventory_product = tk.StringVar()

        ttk.Entry(form, textvariable=self._inventory_index, width=15).grid(row=0, column=1, padx=6, pady=6)
        ttk.Entry(form, textvariable=self._inventory_category, width=18).grid(row=0, column=3, padx=6, pady=6)
        ttk.Entry(form, textvariable=self._inventory_product, width=18).grid(row=0, column=5, padx=6, pady=6)

        ttk.Button(form, text="Assign", command=self._on_assign_inventory).grid(row=0, column=6, padx=6, pady=6)

        self._array_list = tk.Listbox(self._tab_array, height=18)
        self._array_list.pack(fill="both", expand=True, padx=10, pady=10)

    def _on_enqueue_order(self) -> None:
        code = self._order_code.get().strip()
        customer = self._order_customer.get().strip()
        category = self._order_category.get().strip()

        if not code or not customer or not category:
            messagebox.showwarning("Missing data", "Complete code, customer, and category.")
            return

        self._service.register_order(code=code, customer=customer, category=category)
        self._order_code.set("")
        self._order_customer.set("")
        self._order_category.set("")
        self._refresh_queue()

    def _on_serve_order(self) -> None:
        order = self._service.serve_order()
        if order is None:
            messagebox.showinfo("Empty queue", "No orders to serve.")
            return

        messagebox.showinfo("Order served", f"Served: {order.code} - {order.customer}")
        self._refresh_queue()

    def _on_push_package(self) -> None:
        code = self._package_code.get().strip()
        destination = self._package_destination.get().strip()

        if not code or not destination:
            messagebox.showwarning("Missing data", "Complete code and destination.")
            return

        self._service.load_package(code=code, destination=destination)
        self._package_code.set("")
        self._package_destination.set("")
        self._refresh_stack()

    def _on_pop_package(self) -> None:
        package = self._service.unload_package()
        if package is None:
            messagebox.showinfo("Empty stack", "No packages to unload.")
            return

        messagebox.showinfo("Package unloaded", f"Unloaded: {package.code} ({package.destination})")
        self._refresh_stack()

    def _on_assign_inventory(self) -> None:
        index_text = self._inventory_index.get().strip()
        category = self._inventory_category.get().strip()
        product = self._inventory_product.get().strip()

        if not index_text or not category or not product:
            messagebox.showwarning("Missing data", "Complete index, category, and product.")
            return

        try:
            index = int(index_text)
            self._service.assign_inventory(index=index, category=category, product=product)
        except ValueError:
            messagebox.showerror("Invalid index", "Index must be numeric.")
            return
        except IndexError as exc:
            messagebox.showerror("Out of range", str(exc))
            return

        self._inventory_index.set("")
        self._inventory_category.set("")
        self._inventory_product.set("")
        self._refresh_array()

    def _refresh_all(self) -> None:
        self._refresh_queue()
        self._refresh_stack()
        self._refresh_array()

    def _refresh_queue(self) -> None:
        self._queue_list.delete(0, tk.END)
        for i, order in enumerate(self._service.list_orders(), start=1):
            item = f"{i}. [{order.code}] {order.customer} - {order.category}"
            self._queue_list.insert(tk.END, item)

    def _refresh_stack(self) -> None:
        self._stack_list.delete(0, tk.END)
        load = self._service.list_load()
        for pos, package in enumerate(reversed(load), start=1):
            item = f"{pos}. [{package.code}] {package.destination}"
            self._stack_list.insert(tk.END, item)

    def _refresh_array(self) -> None:
        self._array_list.delete(0, tk.END)
        for index, slot in enumerate(self._service.get_inventory()):
            if slot is None:
                item = f"{index}: (empty)"
            else:
                item = f"{index}: {slot.category} -> {slot.product}"
            self._array_list.insert(tk.END, item)
