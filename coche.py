class coche:
	def __init__(self,marca,precio,color):
		self.marca=marca
		self.color=color
		self.precio=precio
	def prender(self):
		print(f"el {self.marca} esta encendido")
	def apagar(self):
		print(f"el {self.marca} esta apagado")
	def acelerar(self):
		print(f"el {self.marca} esta acelerando")

coche1=coche("kia","negro",2000)
coche1.prender()
coche1.apagar()
coche1.acelerar()

