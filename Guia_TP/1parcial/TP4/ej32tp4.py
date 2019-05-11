terminos = int(input("Terminos: "))

a, u, i = 0, 1, 0 

while(i < terminos): 
    print(a, end = ', ') 
    a = u - a
    u += a
    i += 1