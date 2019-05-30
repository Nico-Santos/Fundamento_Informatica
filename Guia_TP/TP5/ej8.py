def mcd(a, b):
    i, d = 1, 1
    
    if(a > b):
        n = a - b
    elif(a == b):
        d = a
        n = 0
    else:
        n = b - a

    while(i <= n):
        if((a % i) == 0 and (b % i) == 0):
            d = i
        i += 1
    
    return d
        
a = int(input("Numero1: "))
b = int(input("Numero2: "))

print(mcd(a, b))