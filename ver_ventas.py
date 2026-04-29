def ver_ventas(ventas):
    if not ventas:
        print("📭 No hay ventas registradas.")
        return

    print("\n📊 LISTADO DE VENTAS")
    print("-" * 50)

    # Encabezados
    print(f"{'ID':<5}{'Producto':<20}{'Cantidad':<10}{'Precio':<10}")
    print("-" * 50)

    # Datos
    for i, venta in enumerate(ventas):
        print(f"{i:<5}{venta['producto']:<20}{venta['cantidad']:<10}{venta['precio']:<10.2f}")

    print("-" * 50)

   #prueba fallas test 
    assert "IMPRESORA" in salida