import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from unittest.mock import patch
import menu_principal


# Testea que mostrar_menu devuelve lo ingresado
def test_mostrar_menu():
    with patch("builtins.input", return_value="1"):
        opcion = menu_principal.mostrar_menu()
        assert opcion == "1"


# Testea salir del programa
def test_main_salir(capsys):
    with patch("builtins.input", side_effect=["5"]):
        menu_principal.main()

    captured = capsys.readouterr()
    assert "Saliendo del programa..." in captured.out