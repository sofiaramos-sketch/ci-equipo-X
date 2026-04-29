import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from unittest.mock import patch


def test_base():
    assert True



# MENU PRINCIPAL
menu_principal = pytest.importorskip("menu_principal")

def test_mostrar_menu():
    with patch("builtins.input", return_value="1"):
        assert menu_principal.mostrar_menu() == "1"


def test_main_salir(capsys):
    with patch("builtins.input", side_effect=["5"]):
        menu_principal.main()
    assert "Saliendo del programa" in capsys.readouterr().out

# AGREGAR VENTA
agregar_venta = pytest.importorskip("agregar_venta")

def test_agregar_venta_ok(capsys):
    ventas = []
    with patch("builtins.input", side_effect=["Notebook", "2", "1500"]):
        agregar_venta.agregar_venta(ventas)
    assert len(ventas) == 1


# CALCULAR TOTAL
calcular_total = pytest.importorskip("calcular_total")


def test_calcular_total_con_ventas(capsys):
    ventas = [
        {"producto": "Mouse", "cantidad": 2, "precio": 500},
        {"producto": "Teclado", "cantidad": 1, "precio": 2000},
    ]

    calcular_total.calcular_total(ventas)
    assert "3000.00" in capsys.readouterr().out


def test_calcular_total_sin_ventas(capsys):
    ventas = []
    calcular_total.calcular_total(ventas)

    assert "No hay ventas" in capsys.readouterr().out


def test_calcular_total_sin_ventas(capsys):
    ventas = []

    calcular_total.calcular_total(ventas)

    captured = capsys.readouterr()
    assert "No hay ventas" in captured.out


# ELIMINAR VENTA

eliminar_venta = pytest.importorskip("eliminar_venta")

def test_eliminar_venta_ok():
    ventas = [{"producto": "Mouse", "cantidad": 2, "precio": 500.0}]
    with patch("builtins.input", side_effect=["Mouse", "2", "500"]):
        eliminar_venta.eliminar_venta(ventas)
    assert len(ventas) == 0

# VER VENTAS
ver_ventas = pytest.importorskip("ver_ventas")


def test_ver_ventas_con_datos(capsys):
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
    ventas = []
    ver_ventas.ver_ventas(ventas)

    assert "No hay ventas" in capsys.readouterr().out
def test_ver_ventas_sin_datos(capsys):
    ventas = []

    ver_ventas.ver_ventas(ventas)

    captured = capsys.readouterr()
    assert "No hay ventas" in captured.out
