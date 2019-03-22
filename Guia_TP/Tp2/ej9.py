#Programa: ej9.py
#Descripcion: imprimir cantidad de billetes equivalentes
#Autor: Nicolas Santos
#Fecha: 19/03/19

# -*- coding: utf-8 -*-

def billetes(dinero):
    cien = dinero / 100
    cincuenta = (dinero % 100) / 50
    diez = ((dinero % 100) % 50) / 10
    cinco = (((dinero % 100) % 50) % 10) / 5
    uno = (((dinero % 100) % 50) % 10) % 5
    print("Billetes de $100: %d" % cien)
    print("Billetes de $50: %d" % cincuenta)
    print("Billetes de $10: %d" % diez)
    print("Billetes de $5: %d" % cinco)
    print("Billetes de $1: %d" % uno)


billetes(166)