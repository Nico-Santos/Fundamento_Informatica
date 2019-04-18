def signo(n):
    if(n > 0):
        return 1
    elif(n < 0):
        return -1
    else:
        return 0
    
n = int(input("Numero: "))
print(signo(n))