# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class pelicula:
    def __init__(self,titulo,genero,nacionalidad):
        self.titulo=titulo
        self.genero=genero
        self.nacionalidad=nacionalidad
        
    def recaudar(self,dinero):
        print(f"la pelicula: {self.titulo} recaudo: ",dinero," de dolares ")
    def duracion(self,hora):
        print(f"la pelicula: {self.titulo} tiene una duracion de: ",hora," minutos")
   

pelicula1=pelicula("Mario Bross", "ciencia ficcion", "Estados Unidos")
print("TITULO:",pelicula1.titulo)
print("GENERO",pelicula1.genero)
print("NACIONALIDAD",pelicula1.nacionalidad)
print(pelicula1.nacionalidad)
dinero=float(input("ingrese la recaudacion global de la pelicula "))
pelicula1.recaudar(dinero)
hora=float(input("ingrese la duracion de la pelicula "))
pelicula1.duracion(hora)
