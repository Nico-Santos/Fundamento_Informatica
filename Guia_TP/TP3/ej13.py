#Calcula sueldo de un empleado en base a sueldo y antiguedad

print("Calculo del salario de un empleado\n")

sueldo_basico = float(input("Sueldo basico del empleado: "))
if(sueldo_basico <= 0):
    print("Dato no valido")
else:
    jubilacion = sueldo_basico * 0.11
    obra_social = sueldo_basico * 0.03
    sindicato = sueldo_basico * 0.03
    
    antiguedad = int(input("Antigüedad del empleado: "))
    if(antiguedad < 0):
        print("Dato no valido")
    else:
        estado_civil = input("Estado civil: soltero(s) o casado(c)): ")
        if(estado_civil == 's'):
            sueldo = sueldo_basico + antiguedad * 0.05 
            print("\nDescuento jubilacion: $", -jubilacion)
            print("Descuento obra social: $",-obra_social)
            print("Descuento sindicato: $", -sindicato)
            print("Sueldo basico: $", sueldo_basico)
            print("Sueldo neto: $", sueldo - jubilacion - obra_social - sindicato)

        elif(estado_civil == 'c'):
            sueldo = sueldo_basico + antiguedad * 0.07
            print("\nDescuento jubilacion: $", -jubilacion)
            print("Descuento obra social: $",-obra_social)
            print("Descuento sindicato: $", -sindicato)
            print("Sueldo basico: $", sueldo_basico)
            print("Sueldo neto: $", sueldo - jubilacion - obra_social - sindicato)

        else:
            print("Dato no valido")




