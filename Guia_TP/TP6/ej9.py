#Carga de modulo
import random

#Inicializacion de variables
lista = []
listaBool = []

#Ingresa largo de lista
N = int(input("Ingrese largo de lista: "))

#Carga nros en "lista"
for i in range(N):
    lista.append(random.randint(0, 10))
    
for i in range(len(lista)-1):
    if(lista[i] < lista[i+1]):
        listaBool.append(True)
    else:
        listaBool.append(False)

print("Lista armada:", lista)
print("Lista booleana:", listaBool)