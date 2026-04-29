def mostrar_menu():
    print("\n=== Menú Principal de Ventas ===")
    print("1. Agregar ventas")
    print("2. Ver ventas")
    print("3. Eliminar ventas")
    print("4. Calcular total de ventas")
    print("5. Salir")
    return input("Selecciona una opción: ")

# Intentar importar funciones de otros módulos catch and try
try:
    from agregar_venta import agregar_venta
except ImportError:
    def agregar_venta(ventas):
        print("Módulo 'agregar_venta' no disponible.")

try:
    from ver_ventas import ver_ventas
except ImportError:
    def ver_ventas(ventas):
        print("Módulo 'ver_ventas' no disponible.")

try:
    from eliminar_venta import eliminar_venta
except ImportError:
    def eliminar_venta(ventas):
        print("Módulo 'eliminar_venta' no disponible.")

try:
    from calcular_total import calcular_total
except ImportError:
    def calcular_total(ventas):
        print("Módulo 'calcular_total' no disponible.")

def main():
    ventas = []  # Lista para almacenar ventas
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            agregar_venta(ventas)
        elif opcion == "2":
            ver_ventas(ventas)
        elif opcion == "3":
            eliminar_venta(ventas)
        elif opcion == "4":
            calcular_total(ventas)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main() 