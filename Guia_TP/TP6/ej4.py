#Invertir nros en posiciones impares

lista = [1, 2, 3, 4, 5]
aux, i = 0, 0

print("Original:", lista)

if(len(lista) % 2 != 0):
    while(i < (len(lista)-1)):
        aux = lista[i]
        lista[i] = lista[i+2]
        lista[i+2] = aux
        i += 2
else:
    while(i < (len(lista)-2)):
        aux = lista[i]
        lista[i] = lista[i+2]
        lista[i+2] = aux
        i += 2
    
print("Invertida:", lista)