def comparar_2enteros(a, b):
    if(a > b):
        return 1
    elif(a < b):
        return -1
    else:
        return 0
    
a = int(input("Numero: "))
b = int(input("Numero: "))

print(comparar_2enteros(a, b))