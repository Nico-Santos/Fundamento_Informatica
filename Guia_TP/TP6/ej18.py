import random, func6

list =[]
n = int(input("cantidad: "))
suma = 0

while(n >= 0):
    if(n > 0):
        ele = random.randint(1,20)
        suma += ele
        if(suma <= 20):
            list.append(ele)
            n -= 1
        else:
            suma = 0
            list.append(suma)
    else:
        list.append(0)
        n -= 1
        
print(list)

print(func6.secuenciaMax(list))