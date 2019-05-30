#Inicializacion de variables
lista = [5, 4, 2, 1, 0]
i = 0
#--------------------------------------

#Nro a agregar en lista ordenada
nro = int(input("Ingrese numero a agregar: "))

#--------------------------------------

#Muestra lista original
print("Lista dada:", lista)

#Corrobora si es ascendente
if(lista[0] < lista[1]):
    #Recorre lista
    while(i < len(lista) and i != -1):
        #Agrega valor de < a >        
        if(nro < lista[i]):
            lista.insert(i, nro)
            i = -1
        #Agrega al final si no hay antes
        elif(i == len(lista)):
            lista.append(nro)
            i = -1
        else:
            i += 1
#Corrobora si es descendente
else:
    #Recorre lista
    while(i < len(lista) and i != -1):
        #Agrega valor de > a <
        if(nro > lista[i]):
            lista.insert(i, nro)
            i = -1
        #Agrega al final si no hay antes
        elif(i == len(lista)):
            lista.append(nro)
            i = -1
        else:
            i += 1
    
print("Lista final:", lista)