# -*- coding: utf-8 -*-

#Ej. 5
#Conversion de medidas: metros a (centimetros, pulgadas, pies, yardas)
#Entrada en metros

#Conviene poner valores en una variable para mejor visualizacion
#o asi esta bien?
def conversor_unidades(metros):
    print("Conversion de metros")
    print(("%.2f cm" % (metros * 100)))
    print(("%.2f pulgadas" % (float(metros * 100) / 2.54)))
    print(("%.2f pies" % (float(metros * 3.28))))
    print(("%.2f yardas" % (float(metros / 0.914))))

conversor_unidades(1)