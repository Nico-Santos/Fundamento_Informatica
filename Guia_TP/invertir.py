def invertirNumero(nro):
    res = 0
    while(nro > 0):
        res = 10 * res + nro % 10
        nro //= 10
    return res

print(invertirNumero(123))