#Ingresar conjunto de numeros y ver
#si la cantidad es par o impar
#SIN USAR CONTADORES

numeros = []
dato_ingresado = 0

while( dato_ingresado != -1):
    dato_ingresado = float(input("Ingrese un numero: "))
    if(dato_ingresado == -1):
        if((len(numeros)) == 0):
            print("No ha ingresado valores")
        elif((len(numeros)) % 2 == 0):
            print("Ha ingresado una cantidad par de elementos")
        else:
            print("Ha ingresado una cantidad impar de elementos")
    else:
        numeros.append(dato_ingresado)
