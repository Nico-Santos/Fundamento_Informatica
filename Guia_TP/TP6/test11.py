#Inicializacion de variables
lista = [5, 3, 2]
aux = []
i, j = 0, 0
#--------------------------------------

#Nro a agregar en lista ordenada
nro = int(input("Ingrese numero a agregar: "))

#--------------------------------------

#Muestra lista original
print("Lista dada:", lista)

#Corrobora si es ascendente
if(lista[0] < lista[1]):
    #Recorre lista
    while(i < len(lista)):
        #Agrega valor si "nro" es menor que el que esta en la lista dada
        #Como "nro" lo tiene que ingresar una sola vez, uso un flag para
        #ver si ya lo agrego o no. Y no aumento el indice i porque estaria
        #agregando un NUEVO ELEMENTO por lo que tiene que la lista "aux"
        #tiene que tener 1 ELEMENTO MAS que la dada.
        if(nro < lista[i] and j == 0):
            aux.append(nro)
            j = -1
        #Si el numero de la lista dada es mayor o igual que el "nro"
        #ingresado O el "nro" dado es mayor que el de la lista dada,
        #agrego el elemento de la LISTA DADA y ahora si incremento
        #el indice i en 1 porque era parte de la LISTA DADA.
        if(lista[i] >= nro or nro > lista[i]):
            aux.append(lista[i])
            i += 1
    #Si hasta aca no se agrego el "nro" que quiero, lo agrego al final
    if(i == len(lista) and j == 0):
        aux.append(nro)
else:
    while(i < len(lista)):
        if(nro > lista[i] and j == 0):
            aux.append(nro)
            j = -1
        if(lista[i] <= nro or nro < lista[i]):
            aux.append(lista[i])
            i += 1
    if(i == len(lista) and j == 0):
        aux.append(nro)
        
print("Lista final:", aux)