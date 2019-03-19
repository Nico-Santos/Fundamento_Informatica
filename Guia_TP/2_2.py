#Ejercicio 2
def suma_y_diferencia(a, b):
	print("Suma =", a + b)
	print("Diferencia =", a - b)

i = 0
while(i == 0):
 try:
 	a = int(input("Ingrese numero a: "))
 	b = int(input("Ingrese numero b: "))
 	suma_y_diferencia(a, b)
 	i = 1
 	break

 except:
	 print("Error, no es un numero. Intente 	 		   	otra vez")
	 i = 0
	
