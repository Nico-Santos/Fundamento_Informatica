def secuenciaMax(lista):
    j, cant, pos = 0, 0, 0
    limiteSup, ceros = 0, 0
    limiteInf = 0
    posicion = []
    
    while( j < len(lista) ):
        if(lista[j] != 0):
           cant += 1 
        else:
            posicion.append(cant)
            cant = 0
        j += 1
    #todo ok
    for i in range(len(posicion)):
        if(max(posicion) == posicion[i]):
            pos = i
    #todo ok
    for i in range(pos+1):
        limiteSup += posicion[i]
        
        if(i != pos):
            limiteInf += posicion[i]
        
        if(i != 0 and i != pos+1):
            ceros += 1
    
    print(posicion)
    print(limiteSup, limiteInf)
    print(ceros)
    
    return(lista[limiteInf+ceros:limiteSup+ceros])
    
    
lista = [1, 0, 1, 2, 3, 4, 0, 1, 2, 3, 0]
print(secuenciaMax(lista))