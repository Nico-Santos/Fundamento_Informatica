#Verificar si la fecha ingresada (dd/mm/aa) es valida
print("Verificacion de la fecha que introduzca\n")

anio = int(input("Ingrese un año: "))

if( anio >= 1900):
    mes = int(input("Ingrese un mes del año: "))
    if( mes >= 1 and mes <= 12):
        dia = int(input("Ingrese un dia del año: "))
        if( dia >= 1 and dia <= 31):
            if( mes == 2 and dia <= 29):
                if( (anio % 4) == 0 and (anio % 400) == 0 and dia == 29):
                    print("La fecha que ingreso es valida")
                elif( (anio % 4) != 0 and (anio % 400) != 0 and dia == 29):
                    print("La fecha que ingreso no es valida")
        else:
            print("Dato no valido")
     else:
        print("Dato no valido")
else:
    print("Dato no valido")
          
            



                
