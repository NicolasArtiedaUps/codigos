class mascota:
    def __init__(self,nombre,raza,edad):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
    def comer(self):
        print(f"la mascota: {self.nombre} esta comiendo")
    def jugar(self):
        print(f"la mascota: {self.nombre} esta jugando")
    def dormir(self):
        print(f"la mascota: {self.nombre} esta durmiendo")

mascota1=mascota("rex","dalmata",3)
mascota1.comer()
mascota1.jugar()
mascota1.dormir()
