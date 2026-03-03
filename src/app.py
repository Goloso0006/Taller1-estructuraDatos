"""Arranque de la aplicación con interfaz Tkinter."""

import os
import sys
from pathlib import Path

from src.servicios.logistica_service import LogisticaService


def _configure_tk_environment() -> None:
    if os.environ.get("TCL_LIBRARY") and os.environ.get("TK_LIBRARY"):
        return

    candidate_tcl_roots = [
        Path(sys.base_prefix) / "tcl",
        Path(sys.prefix) / "tcl",
        Path.home() / "AppData" / "Local" / "Programs" / "Python" / "Python314" / "tcl",
        Path("C:/Python314/tcl"),
    ]

    for root in candidate_tcl_roots:
        tcl_dir = root / "tcl8.6"
        tk_dir = root / "tk8.6"
        if tcl_dir.exists() and tk_dir.exists():
            os.environ.setdefault("TCL_LIBRARY", str(tcl_dir))
            os.environ.setdefault("TK_LIBRARY", str(tk_dir))
            return


_configure_tk_environment()

from src.ui.app_window import LogisticaWindow


class AppBootstrap:
    """Composición principal de la aplicación bajo POO."""

    def __init__(self) -> None:
        self._service = LogisticaService(capacidad_inventario=10)
        self._window = LogisticaWindow(service=self._service)

    def run(self) -> None:
        self._window.mainloop()


def main() -> None:
    app = AppBootstrap()
    app.run()
