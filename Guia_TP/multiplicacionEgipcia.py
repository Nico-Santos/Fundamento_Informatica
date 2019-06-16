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