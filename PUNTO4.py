# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:12:06 2022

@author: asanjuan14
"""

taller1 = float (input('ingrese nota del taller 1 ' ))
taller2 = float (input('ingrese nota del taller 2 ' ))
taller3 = float (input('ingrese nota del taller 3 ' ))

examen = float (input('ingrese nota del examen en clase ' ))
proyecto = float (input('ingrese nota del proyecto final ' ))


notatalleres=(taller1+taller2+taller3)/3
notat=notatalleres*0.5
notae=examen*0.30
notap=proyecto*0.20

notafinal=notat+notae+notap

print("calificacion final ", notafinal)