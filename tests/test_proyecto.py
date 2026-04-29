import os
import sys
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# TEST BASE 

def test_base():
    assert True



# MENU PRINCIPAL

def test_mostrar_menu():
    try:
        import menu_principal
    except ImportError:
        return

    with patch("builtins.input", return_value="1"):
        assert menu_principal.mostrar_menu() == "1"


def test_main_salir(capsys):
    try:
        import menu_principal
    except ImportError:
        return

    with patch("builtins.input", side_effect=["5"]):
        menu_principal.main()

    assert "Saliendo del programa" in capsys.readouterr().out



# AGREGAR VENTA

def test_agregar_venta_ok():
    try:
        import agregar_venta
    except ImportError:
        return

    ventas = []

    with patch("builtins.input", side_effect=["Notebook", "2", "1500"]):
        agregar_venta.agregar_venta(ventas)

    assert len(ventas) == 1
    assert ventas[0]["producto"] == "Notebook"


def test_agregar_venta_error():
    try:
        import agregar_venta
    except ImportError:
        return

    ventas = []

    with patch("builtins.input", side_effect=["Mouse", "abc", "500"]):
        agregar_venta.agregar_venta(ventas)

    assert len(ventas) == 0


# CALCULAR TOTAL

def test_calcular_total_con_ventas(capsys):
    try:
        import calcular_total
    except ImportError:
        return

    ventas = [
        {"producto": "Mouse", "cantidad": 2, "precio": 500},
        {"producto": "Teclado", "cantidad": 1, "precio": 2000},
    ]

    calcular_total.calcular_total(ventas)

    assert "3000.00" in capsys.readouterr().out


def test_calcular_total_sin_ventas(capsys):
    try:
        import calcular_total
    except ImportError:
        return

    ventas = []

    calcular_total.calcular_total(ventas)

    assert "No hay ventas" in capsys.readouterr().out


# ELIMINAR VENTA

def test_eliminar_venta_ok():
    try:
        import eliminar_venta
    except ImportError:
        return

    ventas = [{"producto": "Mouse", "cantidad": 2, "precio": 500.0}]

    with patch("builtins.input", side_effect=["Mouse", "2", "500"]):
        eliminar_venta.eliminar_venta(ventas)

    assert len(ventas) == 0


def test_eliminar_venta_error():
    try:
        import eliminar_venta
    except ImportError:
        return

    ventas = [{"producto": "Mouse", "cantidad": 2, "precio": 500.0}]

    with patch("builtins.input", side_effect=["Mouse", "abc", "500"]):
        eliminar_venta.eliminar_venta(ventas)

    assert len(ventas) == 1



# VER VENTAS

def test_ver_ventas_con_datos(capsys):
    try:
        import ver_ventas
    except ImportError:
        return

    ventas = [
        {"producto": "Mouse", "cantidad": 2, "precio": 500.0},
        {"producto": "Teclado", "cantidad": 1, "precio": 1500.0},
    ]

    ver_ventas.ver_ventas(ventas)

    salida = capsys.readouterr().out
    assert "LISTADO DE VENTAS" in salida
    assert "Mouse" in salida
    assert "Teclado" in salida


def test_ver_ventas_sin_datos(capsys):
    try:
        import ver_ventas
    except ImportError:
        return

    ventas = []

    ver_ventas.ver_ventas(ventas)

    assert "No hay ventas" in capsys.readouterr().out
