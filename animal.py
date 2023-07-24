class animal:
	def __init__(self,nombre,tipo_comida,edad):
		self.nombre=nombre
		self.tipo_comida=tipo_comida
		self.edad=edad
	def comer(self):
		print(f"el {self.nombre} esta comiendo")
	def correr(self):
		print(f"el {self.nombre} esta corriendo")
	def dormir(self):
		print(f"el {self.nombre} esta durmiendo")
	def jugar(self):
		print(f"el {self.nombre} esta jugando")

perro=animal("perro","carne",3)
perro.comer()
perro.correr()
perro.jugar()
perro.dormir()