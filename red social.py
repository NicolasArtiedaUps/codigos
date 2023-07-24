
class redSocial:
	def __init__(self,nombre,creador,idiomas,registrados,):
		self.nombre=nombre
		self.creador=creador
		self.idiomas=idiomas
		self.registrados=registrados
	def comunicar(self):
		print(f"el {self.nombre} esta comunicando")
	def funcionar(self):
		print(f"el {self.nombre} esta funcionando")
	def registrar(self):
		print(f"el {self.nombre} esta registrando")
	def monetizar(self):
		print(f"el {self.nombre} esta monetizando")

redSocial1=redSocial("facebook","Mark  Zuckerberg ","multilenguaje","2936 millones")
redSocial1.comunicar()
redSocial1.funcionar()
redSocial1.registrar()
redSocial1.monetizar()
