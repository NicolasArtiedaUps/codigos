class antena:
    def __init__(self,marca,precio,ganancia):
        self.marca=marca
        self.precio=precio
        self.ganancia=ganancia
    def encender(self):
        print("la antena: {self.antena} esta encendida")
    def apagar(self):
        print("la antena: {self.antena} esta apagada")
    def medicion(self):
        print("la antena: {self.antena} esta midiendo")

antena1=antena("direcTV",320,3.80)
antena1.encender()
antena1.apagar()
antena1.medicion()
