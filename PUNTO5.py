# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:18:26 2022

@author: asanjuan14
"""

redes = float (input('Numero de alumnos de redes ' ))
contabilidad = float (input('Numero de alumnos de contabilidad ' ))
diseño = float (input('Numero de alumnos de diseño ' ))

numeroalumnos=redes+contabilidad+diseño


predes=(redes*100)/numeroalumnos
pcontabilidad=(contabilidad*100)/numeroalumnos
pdiseño=(diseño*100)/numeroalumnos


print("porcentaje de estudiantes de redes ",predes)
print("porcentaje de estudiantes de contabilidad ",pcontabilidad)
print("porcentaje de estudiantes de diseño ",pdiseño)
