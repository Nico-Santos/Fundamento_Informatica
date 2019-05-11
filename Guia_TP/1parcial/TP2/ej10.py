#Programa: ej9.py
#Descripcion: convertido F a C
#Autor: Nicolas Santos
#Fecha: 19/03/19

# -*- coding: utf-8 -*-

def convertir_temperatura(f):
    #Escribir 9.0 o castearlo a float
    #Sino error en division
    c = (5 / 9.0) * (f - 32)
    print(("Grados Fahrenheit: %.2f F " % f))
    print(("Grados Celcios %.2f C" % c))

convertir_temperatura(33)