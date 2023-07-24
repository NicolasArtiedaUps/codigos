class robot:
	def __init__(self,marca,color,precio,memoria):
		self.marca=marca
		self.color=color
		self.precio=precio
		self.memoria=memoria
	def encender(self):
		print(f"el {self.marca} esta encendido")
	def apagar(self):
		print(f"el {self.marca} esta apagado")
	def hablar(self):
		print(f"el {self.marca} esta hablando")
	def limpiar(self):
		print(f"el {self.marca} esta limpiando")

robot1=robot("tesla","gris",5000,"1 Terabyte")
robot1.encender()
robot1.apagar()
robot1.hablar()
robot1.limpiar()