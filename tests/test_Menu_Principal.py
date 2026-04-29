from unittest.mock import patch
import Menu_Principal


# Testea que mostrar_menu devuelve lo ingresado
def test_mostrar_menu():
    with patch("builtins.input", return_value="1"):
        opcion = Menu_Principal.mostrar_menu()
        assert opcion == "1"


# Testea salir del programa
def test_main_salir(capsys):
    with patch("builtins.input", side_effect=["5"]):
        Menu_Principal.main()

    captured = capsys.readouterr()
    assert "Saliendo del programa..." in captured.out