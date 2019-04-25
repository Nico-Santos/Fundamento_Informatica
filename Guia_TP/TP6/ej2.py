import func6

def suma_lista(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

lista = func6.in_lista()

print(suma_lista(lista))