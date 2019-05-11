nro = float(input("Ingrese nro: "))
menor = nro
mayor = nro

while(nro < 0):
	print("Ingrese numero positivo")
	nro = float(input("ingrese nro: "))

while(nro != -1):
	if(nro > mayor):
		mayor = nro
	else:
		if(nro >= 0 and nro < menor):
			menor = nro
	nro = float(input("Ingrese nro: "))
	while(nro < -1):
		print("Ingrese numero positivo")
		nro = float(input("ingrese nro: "))
	
	
print("Numero mayor es:", mayor)
print("Numero menor es:", menor)