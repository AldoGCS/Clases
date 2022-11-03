nombre_empleado = input("Nombre? ")
cantidad_ventas = float(input("Cantidad de Ventas? "))
print(f"Tu nombre es: {nombre_empleado} Y has vendido ${cantidad_ventas}")

comision_13 = ((cantidad_ventas * 13) / 100)

print(f"Tu comision de este mes es: ${comision_13}")