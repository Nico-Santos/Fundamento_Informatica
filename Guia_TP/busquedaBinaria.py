lista = [0, 1, 2, 8, 13, 17, 19, 32]

min = 0
max = len(lista)
pos = -1

valor = int(input("Ingrese valor a buscar: "))

while(min <= max and pos == -1):
    valMed = (min + max) // 2
    
    if(valMed != len(lista)):
        if(valor == lista[valMed]):
            pos = valMed
        elif(valor >= lista[valMed]):
            min = valMed + 1
        else:
            max = valMed - 1
    else:
        break

if(pos != -1):
    print("El valor buscado se encuentra en la siguiente posicion:", pos)
else:
    print("El valor buscado no es encuentra en la lista")

#--------------------------------------------------------------    
def busquedaBinaria(lista, buscado):
    min, max = 0, len(lista)
    pos = -1
    while(min <= max and pos == -1):
        valMed = (min + max) // 2
        if(valMed != len(lista)):
            if(buscado == lista[valMed]):
                pos = valMed
            elif(buscado >= lista[valMed]):
                min = valMed + 1
            else:
                max = valMed - 1
        else:
            pos = -1
        return pos
#---------------------------------------------------------------
print("%d" % 12345.54321)

    
    
    
    
    
    