def rusa(multiplicador, multiplicando):
    suma = 0
    if(multiplicador % 2 != 0):
            suma = multiplicando
    while(multiplicador != 1):
        multiplicador //= 2
        multiplicando *= 2
        if(multiplicador % 2 != 0):
            suma += multiplicando
    return suma

print(rusa(37, 12))


def rusa(multiplicador, multiplicando):
    listaSuma = []
    suma = 0
    if(multiplicador % 2 != 0):
            listaSuma.append(multiplicando)
    while(multiplicador != 1):
        multiplicador //= 2
        multiplicando *= 2
        if(multiplicador % 2 != 0):
            listaSuma.append(multiplicando)
    for i in range(len(listaSuma)):
        suma += listaSuma[i]
    return suma

print(rusa(37, 12))