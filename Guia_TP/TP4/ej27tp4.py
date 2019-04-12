nro = int(input("numero a contar: "))

digitos = 1
nro //= 10

while(nro != 0):
	digitos += 1
	nro //= 10
	
print(digitos)