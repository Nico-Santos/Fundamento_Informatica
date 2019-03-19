#Ej. 3a
import math

def sup_circulo(radio):
	print("Superficie del circulo: ", math.pi * (radio**2))

radio = float(input("Ingrese radio: "))

if (radio == 0):
	print("Error, no es un circulo")
else:
	sup_circulo(radio)