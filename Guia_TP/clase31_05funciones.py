'''
Funcion: Cargar X valores en una lista
Parametros: lista, cantidad
Return: N/A
'''
def cargarLista(lista, cantidad):
    import random #---------------------->>>Tendria que ir fuera de la funcion?
    for i in range(cantidad):
        lista.append(random.randint(100, 999))
'''
Funcion: Verifica si existen valores de Fibonacci en la lista
Parametros: lista
Return: Porcentaje de valores encontrados
'''
def estanEnFibonacci(lista):
    a, u, pertenece = 0, 1, 0 
    while(a < maximoNumero(lista)): 
        a = u - a
        u += a
        for i in range(len(lista)):
            if(lista[i] == a):
                pertenece += 1
    return (pertenece*100) / len(lista)
'''
Funcion: Hallar el valor mas grande de una lista
Parametro: lista
Return: El mayor numero
'''
def maximoNumero(lista):
    maximo = lista[0]
    for i in range(len(lista)):
        if(maximo < lista[i]):
            maximo = lista[i]
    return maximo
'''
Funcion: Hallar el valor mas chico de la lista
Parametro: lista
Return: El menor numero
'''
def minimoNumero(lista):
    minimo = lista[0]
    for i in range(len(lista)):
        if(minimo > lista[i]):
            minimo = lista[i]
    return minimo
'''
Funcion: Hallar raices cuadradas de una lista
Parametro: lista
Return: Porcentaje raices encontradas
'''
def promedioRaiz2(lista):
    raiz2, i = 0, 1
    while(i < len(lista)):
        cont = lista[i]
        while(cont > 0):
            if(cont * cont == lista[i]):
                raiz2 += 1
            cont -= 1
        i += 1
    return raiz2 / len(lista)
'''
Funcion: Ordenar ascendentemente una lista
Parametro: lista
Return: La lista ordenada(modificando la original)
'''
def ordenarAsc(lista):
    listaAux = []
    for i in range(len(lista)):
        listaAux.append(minimoNumero(lista))
        lista.remove(minimoNumero(lista))
    for i in range(len(listaAux)):
        lista.append(listaAux[i])
    return lista
'''
Funcion: Verifica si el numero tiene 3 digitos
Parametro: valor
Return: True si tiene 3 digitos, sino False
'''
def tiene3Digitos(valor):
    digitos = 0
    while(valor > 0):
        digitos += 1
        valor //= 10
    if(digitos == 3):
        return True
    else:
        return False
'''
Funcion: Busqueda binaria en una lista
Parametros: lista, buscado
Return: Si no se encontro valor buscado, -1
        Si el valor buscado no tiene 3 digitos, -2
        Si existe, lista de posiciones donde se encuentra el valor
'''
def busquedaBinaria(lista, buscado):
    if(tiene3Digitos(buscado) == True):
        lista = ordenarAsc(lista)
        min, max, pos = 0, len(lista), -1
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
    else:
        return -2
'''
Funcion: Busqueda secuencial en una lista
Parametros: lista, elemento
Return: Lista de posicio/es si existe
        Si no encontro, -1
'''
def busquedaSecuencial(lista, elemento):
    posicion = []
    for i in range(len(lista)):
        if(elemento == lista[i]):
            posicion.append(i)
    if(len(posicion) == 0):
        return -1
    return posicion

def menu():
    print("(1) Cargar lista")
    print("(2) Porcentaje de numeros que pertenecen a la serie de Fibonacci")
    print("(3) Promedio de numeros con raiz cuadrada")
    print("(4) Muestra lista con formato")
    print("(5) Ordenar posiciones multiplos de 3 en forma ascendente")
    print("(6) Buscar numero usando busqueda binaria")
    print("(7) Buscar elemento usando busqueda secuencial")
    print("(8) Muestra menu")
    print("(9) Salir")