#Inicializacion de variables
lista = [1, 2, 3, 4]
producto = 1
suma = 0
aux = []
j = len(lista) - 1

#--------------------------------------

#Calcula producto de elementos en posiciones
#pares de la lista
for i in range(len(lista)):
    if(i % 2 == 0):
        producto *= lista[i]

#--------------------------------------
        
#Calcula suma de elementos en posiciones
#impares de la lista
for i in range(len(lista)):
    if(i % 2 != 0):
        suma += lista[i]

#--------------------------------------

#Muestra lista original
print("Lista:", lista)

#--------------------------------------

#Suma divide a producto si es != 0
#Si = 0, error
if(suma != 0):
    print("La division es:", producto / suma)
else:
    print("Error, no se puede dividir por cero")

#--------------------------------------
    
for i in range(len(lista)//2):
    aux.append(lista[i] + lista[j])
    j -= 1

print("Lista modificada:", aux)