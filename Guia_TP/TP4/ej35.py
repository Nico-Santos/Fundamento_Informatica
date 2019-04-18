#Ejercicio 35

i = 0
soloA = 0
soloB = 0
ambos = 0
ninguno = 0
A = 0
B = 0

while(i < 10):
    producto =  int(input("Acepta o no: "))

    if( (producto // 10) == 1 and (producto % 10) == 0):
        soloA += 1
    elif( (producto // 10) == 0 and (producto % 10) == 1):
        soloB += 1
    elif( (producto // 10) == 1 and (producto % 10) == 1):
        ambos += 1
        A += 1
        B += 1
    else:
        ninguno += 1

    i += 1

print("Solo producto A:", (soloA * 100)/i, end = '%\n')
print("Solo producto B:", (soloB * 100)/i, end = '%\n')
print("Producto A:", (A * 100)/i, end = '%\n')
print("Producto B:", (B * 100)/i, end = '%\n')
print("Ni A ni B:", (ninguno * 100)/i, end = '%\n')
print("A y B:", (ambos * 100)/i, end = '%\n')
    

    
