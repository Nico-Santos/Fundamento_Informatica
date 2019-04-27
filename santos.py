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
me, ma = 0, 0

while(i < 3):
    nro = int(input("Ingreso nro: "))
    #nro = random.randint(10, 99)
    if(nro >= 10 and nro <= 95):
        i += 1
        if(nro < menor):
            menor = nro
            me = i-1
        if(nro > mayor):
            mayor = nro
            ma = i-1
    else:
        print("Ingrese un nro valido")
        

print("\nMenor:", menor, "Pos:", me)
print("Mayor:", mayor, "Pos:", ma, "\n")

cubica, i = 1, 1
me, ma = False, False


while( cubica < mayor):
    cubica = i * i * i
    if(cubica % mayor == 0):
        print("El mayor tiene raiz cubica entera")
        ma = True
    if(cubica % menor == 0):
        print("El menor tiene raiz cubica entera")
        me = True
    i += 1

if(ma == False):
    print("El mayor no tiene raiz cubica entera")
if(me == False):
    print("El menor no tiene raiz cubica entera")