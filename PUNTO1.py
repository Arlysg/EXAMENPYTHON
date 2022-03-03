# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:21:16 2022

@author: asanjuan14


"""


VALORDONADO = float (input('VALOR DONADO '))


telecomunicaciones=VALORDONADO*0.10
sistemas=VALORDONADO*0.25
administracion=VALORDONADO*0.35
sumadonacion=telecomunicaciones+sistemas+administracion
contabilidad=VALORDONADO-sumadonacion

print("valor donado",VALORDONADO)
print("valor para el area de telecomunicaciones",telecomunicaciones)
print("valor para el area de sistemas ",sistemas)
print("valor para e area de administracion",administracion)
print("valor para el area de contabilidad",contabilidad)

