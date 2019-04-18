def termino_central(n):
    i, cont = 0, 1
    while(n // (10 ** i) != 0 and n // (10 ** (i + 1)) != 0):
        cont += 1
        i += 1
    
    if(cont % 2 != 0):
        cont = (cont - 1) / 2
        
        while(cont > 0):
            n //= 10
            cont -= 1
        r = n % 10
        
    else:
        r = -1
    
    return r

n = int(input("Numero: "))
print(termino_central(n))