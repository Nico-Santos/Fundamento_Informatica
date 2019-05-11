#Ej 37 TP4
import random

empleados = 1
total, cantEmp, cantEmpMenos, cantEmpVeinte = 0, 0, 0, 0
menorEmp = 30000
mayorEmp = 1
legajoMasEmp = 0
legajoMenorEmp = 500
impA, impB, impC = 0, 0, 0

while(empleados < 100):
    legajo = random.randint(1, 1000)
    cat = random.randint(ord('A'), ord('C'))
    salario = random.randint(1, 30000)

    total += salario

    if(salario > 20000):
        cantEmpVeinte += 1

    elif(salario < 5000 and chr(cat) == 'C'):
        cantEmpMenos += 1

    elif(salario > mayorEmp):
        mayorEmp = salario
        legajoMasEmp = legajo

    elif(salario < menorEmp):
        menorEmp = salario

    elif(chr(cat) == 'A'):
        impA += salario
    elif(chr(cat) == 'B'):
        impB += salario
    elif(chr(cat) == 'C'):
        impC += salario

    empleados += 1

print("Salario total que paga la empresa:", total, end = '$')
print("\nCantidad mas de 20000:", cantEmpVeinte)
print("Cantidad menos de 5000 y C:", cantEmpMenos)
print("Legajo mas gana:", legajoMasEmp)
print("Total de A:", impA)
print("Total de B:", impB)
print("Total de C:", impC)
print("Salario promedio:", total / empleados, end = '$')
