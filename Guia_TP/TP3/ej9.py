#Devuelve si es bisiesto o no (imprime por pantalla)
def bisiesto(anio):
    if( (anio % 4) == 0 and (anio % 400) == 0):
        print("El año que ingreso", anio, "años es bisiesto")
    else:
        print("El año que ingreso [", anio, "años] no es bisiesto")


anio = int(input("Ingrese un año: "))
bisiesto(anio)
