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

#print(exponencial)
#print(doble)

suma = exponencial[len(exponencial)-1]
j = len(exponencial) - 2
res = doble[len(doble)-1]

while(suma != limite): 
    if((exponencial[j] + suma) <= limite):
        suma += exponencial[j]
        res += doble[j]
        j -= 1
    else:
        j -= 1

print(res)