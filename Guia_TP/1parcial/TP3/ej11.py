#Determinar fecha de Pascua

#Algoritmo de Butcher
anio = int(input("Ingrese fecha: "))
'''
a = anio % 19
b = anio // 100
c = anio % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = ( b - f + 1) // 3
h = (19 * a + b - d - g + 15) % 30
i = c // 4
k = c % 4
l = (32 + 2 * e + 2 * i - h - k) % 7
m = ( a + 11 * h + 22 * l) // 451
n = h + l - (7 * m) + 114
mes = n // 31
dia = 1 + ( n % 31)

print("Pascuas en el año", anio, "es el dia", dia, "/", mes)

'''

a = anio % 19
b = anio % 4
c = anio % 7
d = ((a * 19) + 24 ) % 30
e = (((b * 2) + (c * 4) + (d * 6)) + 5) % 7

if( d + e + 22 < 31):
    print("Menor Fecha Pascua es:", (d + e + 22), "de marzo")
else:
    print("Fecha Pasuca es:", ((d + e + 22) - 31), "de abril")
