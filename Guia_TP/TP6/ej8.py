'''
Mostrar valor minimo y posicion en que
esta en una lista.
Si se repite, mostrar todas las ubicaciones.
'''
#Carga de modulo
import random

#Inicializacion de variables
lista = []
nro = -1
minimo = 100

#Carga nros en "lista" (al azar)
#Para carga con un "0", sin cargarlo
while(nro != 0):
    nro = random.randint(0, 100)
    if(nro != 0):
        lista.append(nro)

#Recorre lista para sacar el nro mas chico
for i in range(len(lista)):
    if(lista[i] < minimo):
        minimo = lista[i]

#Muestra el numero mas chico
print("Numero mas chico de la lista:", minimo)

#Recorre lista para mostrar posicion/es del minimo
for i in range(len(lista)):
    if(lista[i] == minimo):
        print("Posicion:", i)