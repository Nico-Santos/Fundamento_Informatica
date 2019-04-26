'''
ingresar por teclado 30 valores enteros
validar que se encuentre en el rango de 10 a 95
informar en que orden salio el menor y el mayor de ellos
y cuales son de esos valores
obtener la suma de estos e informar si tienen raiz cubica exacta
'''

import random
menor = 95
mayor = 10
i = 1
me = 0
ma = 0


while(i < 5):
    nro = int(input("Ingreso nro: "))
    if(nro >= 10 and nro <= 95):
        i += 1
        if(nro < menor):
            menor = nro
            me = i-1
        if(nro > mayor):
            mayor = nro
            ma = i-1
        

print("Mayor:", mayor, "Pos:", ma)
print("Menor:", menor, "Pos:", me)

if(mayor == 27 or mayor == 64):
    print("El mayor tiene raiz cubica entera")
else:
    print("El mayor no tiene raiz cubica entera")

if(menor == 27 or menor == 64):
    print("El menor tiene raiz cubica entera")
else:
    print("El menor no tiene raiz cubica entera")
    

