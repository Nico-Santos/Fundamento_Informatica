def mostrar_digito(n, i):
    if( n // (10 ** i) == 0 and n // (10 ** (i + 1)) == 0):
        r = n
    else:
        r = n % (10 ** i)
    
    return r

n = int(input("Numero :"))
i = int(input("Digito :"))

print(mostrar_digito(n, i))