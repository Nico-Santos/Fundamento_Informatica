#Ingresa valores a una lista entre 1 y 20
def in_lista():
    lista = []
    print("Ingresando -1 termina")
    dato = float(input("Nro entre 1 y 20: "))
    while(dato != -1):
        if(dato >= 1 and dato <= 20):
            lista.append(dato)
        else:
            print("Fuera de rango")
        
        dato = float(input("Nro entre 1 y 20: "))
    
    return lista

#Suma todos los elementos de una lista
def suma_lista(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

#Calcular cantidad de elementos
def my_len(y):
    c = 0
    for n in y:
        c = c + 1
    return c

#Devuelve si es o no capicua
def capicua(lista):
    i, c = my_len(lista), 0
    for x in lista:
        if(lista[i-1] == lista[c]):
            i -= 1
            c += 1
        else:
            return False
    return True

#Busca valor en una lista y devuelve
#posicion si esta
def buscar_valor(n, lista):
    i = 0
    for x in lista:
        if(lista[i] == n):
            return i
        else:
            i += 1
    return -1