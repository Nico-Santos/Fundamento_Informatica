def mcd(a, b):
    i, d = 1, 1
    
    if(a > b):
        n = b
    else:
        n = a

    while(i < n):
        if((a % i) == 0 and (b % i) == 0):
            d = i
        i += 1
    return d
        
a = int(input("Numero: "))
b = int(input("Numero: "))

print(mcd(a, b))