# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class arbol:
    def __init__(self,nombre,tamaño,forma):
        self.nombre=nombre
        self.tamaño=tamaño
        self.forma=forma
        
    def generar(self):
        print(f"el arbol : {self.nombre} genera oxigeno cada 24 Horas ")
    def exhalar(self):
        print(f"el arbol: {self.nombre} exhala aire para 4 personas")
    def inhala(self,x):
        print(f"el arbol: {self.nombre} inhala un promedio de ",x,"kg de CO2")
    


""" uso de la clase arbol"""

arbol1=arbol("Arbol Kiri",27, "corazon")
print(arbol1.nombre)
arbol1.exhalar()
arbol1.generar()
arbol1.inhala(21.7)