#Carga de modulo
import random

#--------------------------------------

#Inicializacion de variables
listaA = []
listaB = []
listaC = []
listaD = []
listaE = []
j = 0
#--------------------------------------

#Ingresa largo de "A"
N = int(input("Ingrese largo de listaA: "))
#Carga nros en "A"
for i in range(N):
    listaA.append(random.randint(1, 10))

#Ingresa largo de "B"
N = int(input("Ingrese largo de listaB: "))
#Carga nros en "lista"
for i in range(N):
    listaB.append(random.randint(0, 10))

#---------------------------------------

#Muestra lista "A" y "B"
print("Lista A:", listaA)
print("Lista B:", listaB)

#---------------------------------------

#Concatenacion de valores pares de "A"
#con valores impares de "B", en lista "C"

#Cargo en "C" los pares de "A"
for i in range(len(listaA)):
    if(listaA[i] % 2 == 0):
        listaC.append(listaA[i])
#Cargo en "C" los impares de "B"
for i in range(len(listaB)):
    if(listaB[i] % 2 != 0):
        listaC.append(listaB[i])

#Muestra lista "C"
print("Lista C:", listaC)

#--------------------------------------

#Concatenacion de valores pares de "A"
#con reverso de valores pares de "B"
#en "D"

#Cargo en "D" los pares de "A"
for i in range(len(listaA)):
    if(listaA[i] % 2 == 0):
        listaD.append(listaA[i])
#Cargo en "D" los pares de "B" (final a principio)
for i in range((len(listaB)-1), -1, -1):
    if(listaB[i] % 2 == 0):
        listaD.append(listaB[i])

#Muestra lista "D"
print("Lista D:", listaD)

#--------------------------------------

#Intercalacion de elementos
# "A" y "B" en "E"
while(j < len(listaA) or j < len(listaB)):
    if(j < len(listaA)):
        listaE.append(listaA[j])
    if(j < len(listaB)):
        listaE.append(listaB[j])
    j += 1

print("Lista E:", listaE)