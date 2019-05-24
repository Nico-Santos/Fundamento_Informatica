def buscar_valor(n, lista):
    i = 0
    for x in lista:
        if(lista[i] == n):
            return i
        else:
            i += 1
    return -1

print(buscar_valor(6, [1, 2, 3, 6, 8, 10]))