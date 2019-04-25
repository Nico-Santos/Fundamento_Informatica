from func6 import my_len

def capicua(lista):
    i, c = my_len(lista), 0
    for x in lista:
        if(lista[i-1] == lista[c]):
            i -= 1
            c += 1
        else:
            return False
    return True


lista = [4, 2, 2, 1]
print(capicua(lista))

