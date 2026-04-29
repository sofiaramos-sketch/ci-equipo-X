def eliminar_venta(ventas):
    if not ventas:
        print("No hay ventas registradas para eliminar.")
        return

    producto = input("Ingrese el nombre del producto a eliminar: ")
    
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
    except ValueError:
        print("❌ Error: cantidad o precio inválido")
        return

    # Buscar la venta que coincida exactamente
    for i, venta in enumerate(ventas):
        if (venta['producto'] == producto and
            venta['cantidad'] == cantidad and
            venta['precio'] == precio):
            ventas.pop(i)
            print("✅ Venta eliminada correctamente")
            return

    print("❌ No se encontró una venta que coincida exactamente con los datos ingresados.")