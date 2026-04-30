def agregar_venta(ventas):
    producto = input("Ingrese el nombre del producto: ")
    
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
    except ValueError:
        print("❌ Error: cantidad o precio inválido")
        return

    venta = {
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio
    }

    ventas.append(venta)
    print("✅ Venta agregada correctamente")
