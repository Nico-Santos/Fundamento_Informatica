'''
exponencial = []
doble = []
inicial = int(input("Inicial: "))
limite = int(input("Limite: "))
exp = 0
suma = 0
du = 1

while(suma < limite):
    exponencial.append(2**exp)
    suma += (2**exp)
    exp += 1
    doble.append(inicial*du)
    du *= 2

suma = len(exponencial) - 1
j = len(exponencial) - 2

while(suma != limite):    
    if((exponencial[j] + suma) <= limite):
        suma += exponencial[j]
        j -= 1
    else:
        j -= 1
print(suma * inicial)
'''

def egipcia(inicial, limite):
    exponencial = []; doble = []
    exp, suma, du = 0, 0, 1
    while(suma < limite):
        exponencial.append(2**exp)
        suma += (2**exp)
        exp += 1
        doble.append(inicial*du)
        du *= 2
    suma = len(exponencial) - 1
    du = len(exponencial) - 2
    while(suma != limite):    
        if((exponencial[du] + suma) <= limite):
            suma += exponencial[du]
            du -= 1
        else:
            du -= 1
    return (suma * inicial)

inicial = int(input("Inicial: "))
limite = int(input("Limite: "))
print(egipcia(inicial, limite))