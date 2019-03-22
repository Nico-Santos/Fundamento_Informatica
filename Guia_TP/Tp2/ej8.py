#Programa: ej7.py
#Descripcion: calcula segundos en dias, horas, minutos y segundos
#Autor: Nicolas Santos
#Fecha: 19/03/19

# -*- coding: utf-8 -*-

def convertir_segundos(segundos):
    dia = segundos / 86400
    hs = (segundos % 86400) / 3600
    minu = ((segundos % 86400) % 3600) / 60
    seg = ((segundos % 86400) % 3600) % 60

    print("%d dia/s - %d horas - %d minutos - %d segundos" % (dia, hs, minu, seg) )


convertir_segundos(200000)