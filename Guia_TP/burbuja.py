'''
#Burbuja basisco
lista = [9, 56, 5, -6, 0]

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if(lista[i] > lista[j]):
            aux = lista[j]
            lista[j] = lista[i]
            lista[i] = aux            

print(lista)

#Burbuja optimizado
lista = [9, 1, 5, 10, 0]
changes = True
j = 0
while(changes):
    changes = False
    for i in range(len(lista)-1-j):
        if(lista[i] > lista[i+1]):
            aux = lista[i+1]
            lista[i+1] = lista[i]
            lista[i] = aux
            changes = True
    j += 1
            
print(lista)
'''

import random


print(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
print(random.choice('-_.;,/"\"'))
print(random.choice('0123456789'))

























