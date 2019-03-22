#Programa: ej6.py
#Descripcion: calcula promedio de 3 numeros enteros
#Autor: Nicolas Santos
#Fecha: 19/03/19

# -*- coding: utf-8 -*-

def promedio(a, b, c):
    promedio = (a + b + c) / 3.0
    print("Promedio = %.3f" % promedio)


a = int(input("Ingrese un numero entero: "))
b = int(input("Ingrese un numero entero: "))
c = int(input("Ingrese un numero entero: "))

promedio(a, b, c)