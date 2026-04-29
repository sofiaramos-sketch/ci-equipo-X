import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from unittest.mock import patch

# MENU PRINCIPAL
menu_principal = pytest.importorskip("menu_principal")


def test_mostrar_menu():
    with patch("builtins.input", return_value="1"):
        assert menu_principal.mostrar_menu() == "1"


def test_main_salir(capsys):
    with patch("builtins.input", side_effect=["5"]):
        menu_principal.main()

    captured = capsys.readouterr()
    assert "Saliendo del programa..." in captured.out

# AGREGAR VENTA
agregar_venta_mod = pytest.importorskip("agregar_venta")


def test_agregar_venta_ok(capsys):
    ventas = []

    with patch(
        "builtins.input",
        side_effect=["Notebook", "2", "1500"]
    ):
        agregar_venta_mod.agregar_venta(ventas)

    assert len(ventas) == 1
    assert ventas[0]["producto"] == "Notebook"
    assert ventas[0]["cantidad"] == 2
    assert ventas[0]["precio"] == 1500.0

    captured = capsys.readouterr()
    assert "Venta agregada correctamente" in captured.out

    # CALCULAR TOTAL
calcular_total_mod = pytest.importorskip("calcular_total")


def test_calcular_total_con_ventas(capsys):
    ventas = [
        {"producto": "Mouse", "cantidad": 2, "precio": 500},
        {"producto": "Teclado", "cantidad": 1, "precio": 2000},
    ]

    calcular_total_mod.calcular_total(ventas)

    captured = capsys.readouterr()
    assert "3000.00" in captured.out


def test_calcular_total_sin_ventas(capsys):
    ventas = []

    calcular_total_mod.calcular_total(ventas)

    captured = capsys.readouterr()
    assert "No hay ventas registradas" in captured.out

# ELIMINAR VENTA
eliminar_venta_mod = pytest.importorskip("eliminar_venta")


def test_eliminar_venta_ok(capsys):
    ventas = [
        {"producto": "Mouse", "cantidad": 2, "precio": 500.0}
    ]

    with patch(
        "builtins.input",
        side_effect=["Mouse", "2", "500"]
    ):
        eliminar_venta_mod.eliminar_venta(ventas)

    assert len(ventas) == 0

    captured = capsys.readouterr()
    assert "Venta eliminada correctamente" in captured.out


def test_eliminar_venta_no_encontrada(capsys):
    ventas = [
        {"producto": "Mouse", "cantidad": 2, "precio": 500.0}
    ]

    with patch(
        "builtins.input",
        side_effect=["Teclado", "1", "1000"]
    ):
        eliminar_venta_mod.eliminar_venta(ventas)

    assert len(ventas) == 1

    captured = capsys.readouterr()
    assert "No se encontró" in captured.out


def test_eliminar_venta_sin_datos(capsys):
    ventas = []

    eliminar_venta_mod.eliminar_venta(ventas)

    captured = capsys.readouterr()
    assert "No hay ventas registradas" in captured.out


def test_eliminar_venta_error_input(capsys):
    ventas = [
        {"producto": "Mouse", "cantidad": 2, "precio": 500.0}
    ]

    with patch(
        "builtins.input",
        side_effect=["Mouse", "abc", "500"]
    ):
        eliminar_venta_mod.eliminar_venta(ventas)

    assert len(ventas) == 1

    captured = capsys.readouterr()
    assert "Error" in captured.out


    # VER VENTAS
ver_ventas_mod = pytest.importorskip("ver_ventas")


def test_ver_ventas_con_datos(capsys):
    ventas = [
        {"producto": "Mouse", "cantidad": 2, "precio": 500.0},
        {"producto": "Teclado", "cantidad": 1, "precio": 1500.0},
    ]

    ver_ventas_mod.ver_ventas(ventas)

    captured = capsys.readouterr()

    assert "LISTADO DE VENTAS" in captured.out
    assert "Mouse" in captured.out
    assert "Teclado" in captured.out
    assert "500.00" in captured.out
    assert "1500.00" in captured.out


def test_ver_ventas_sin_datos(capsys):
    ventas = []

    ver_ventas_mod.ver_ventas(ventas)

    captured = capsys.readouterr()
    assert "No hay ventas registradas" in captured.out