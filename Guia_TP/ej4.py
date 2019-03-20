# -*- coding: utf-8 -*-

#Ej.  4
# Todos los años tienen 365 dias
def anos_en_dias(edad):
    print("%d año/s = %d dias" % (edad, edad * 365))

edad = int(input("Ingrese su edad(solo años): "))
anos_en_dias(edad)