class celular:
	def __init__(self,marca,color,precio):
		self.marca=marca
		self.color=color
		self.precio=precio
	def encender(self):
		print(f"el {self.marca} esta encendido")
	def apagar(self):
		print(f"el {self.marca} esta apagado")
	def bloquear(self):
		print(f"el {self.marca} esta bloqueado")
	def llamar(self):
		print(f"el {self.marca} esta llamando")

celular1=celular("samsung","verde",380)
celular1.encender()
celular1.apagar()
celular1.bloquear()
celular1.llamar()