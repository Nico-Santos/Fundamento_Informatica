#Mostrar el ultimo valor ingresado que
#esta en una posicion par del array

numeros = []
indice = 0
dato_ingresado = 0

while( dato_ingresado != -1):
    dato_ingresado = float(input("Ingrese un numero: "))
    if(dato_ingresado == -1):
            if(indice == 0):
                print("No ingreso datos")
            elif(indice % 2 == 0):
                print("El ultimo valor es:", numeros[indice - 1])
            elif(indice % 2 != 0 and indice > 1):
                print("El ultimo valor es:", numeros[indice - 2])
            else:
                print("No hay datos a mostrar")
    else:
        indice += 1
        numeros.append(dato_ingresado)
