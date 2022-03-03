# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:56:18 2022

@author: asanjuan14
"""

sueldobase = float (input('ingrese sueldo BASE' ))
ventasmes = float (input('valor de ventas en el mes' ))

comision=ventasmes*0.15

sueldototal=sueldobase+ventasmes

print("valor de comision", comision)
print("sueldo total ",sueldototal)

