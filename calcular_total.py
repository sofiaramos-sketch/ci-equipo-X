def calcular_total(ventas):
    if not ventas:
        print("📭 No hay ventas registradas.")
        return

    total = 0

    for venta in ventas:
        subtotal = venta["cantidad"] * venta["precio"]
        total += subtotal

    print(f"\n💰 Total de ventas: ${total:.2f}")
