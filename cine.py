# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 16:44:45 2023

@author: lab
"""

class cine:
    def __init__(self,nombreCine,numEmpleados,costo_entrada):
        self.nombreCine=nombreCine
        self.numEmpleados=numEmpleados
        self.costo_entrada=costo_entrada
    def emitir(self):
        print("el {self.nombreCine} emite peliculas a las 2 pm")
    def cerrar(self):
        print("el {self.nombreCine} cierra a las 8 pm")
        
        
cine1=cine("multicines", 70, 2.50)
cine1.cerrar()
cine1.emitir()
 
    
   
        