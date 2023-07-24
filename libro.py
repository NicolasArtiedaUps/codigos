class libro:
    def __init__(self,titulo,editorial,precio,autor):
        self.titulo=titulo
        self.editorial=editorial
        self.precio=precio
        self.autor=autor
    def informar(self):
        print(f"el libro: {self.titulo} infoma ")
    def entretener(self):
        print(f"el libro: {self.titulo} entretiene")
    def enseñar(self):
        print(f"el libro: {self.titulo} enseña")

libro1=libro("Algebra de Baldor ","Patria",5.50,"D.G. Terminel y José Luis Mendoza Monroy")
libro1.informar()
libro1.entretener()
libro1.enseñar()
