def extraer_digito(n, i):
    if( n // (10 ** i) == 0 and n // (10 ** (i + 1)) == 0):
        r = -1
    else:
        while(i > 0):
            n //= 10
            i -= 1
        r = n % 10
    
    return r

n = int(input("Numero :"))
i = int(input("Digito :"))

print(extraer_digito(n, i))