#Imprime valor total de venta y precio promedio
#Entradas: cantidad_producto y precio_base
def valor_venta(cantidad_producto, precio_base):
    precio_primera_docena = 0
    precio_10_descuento = 0
    precio_25_descuento = 0

    if(cantidad_producto > 0):
        precio_primera_docena = precio_base * 12
        precio_25_descuento = 0
        if((cantidad_producto - 12) >= 13 and (cantidad_producto - 12 ) <= 100):
            precio_10_descuento = (cantidad_producto - 12) * 90
        elif((cantidad_producto - 12) > 100):
            precio_10_descuento = 88 * 90
            if((cantidad_producto - 12 - 88) > 100):
               precio_25_descuento = (cantidad_producto - 12 - 88) * 75
        else:
            precio_10_descuento = 0

        precio_final = precio_primera_docena + precio_10_descuento + precio_25_descuento
        precio_promedio = precio_final / cantidad_producto
        print("El precio final es:", precio_final)
        print("El precio promedio es: %.2f" % precio_promedio)
            
    else:
        print("Dato", cantidad_producto, "invalido")

cantidad_producto = int(input("Ingrese la cantidad de producto: "))
precio_base = float(input("Ingrese precio base del producto: "))
valor_venta(cantidad_producto, precio_base)
