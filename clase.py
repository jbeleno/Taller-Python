class Persona:
	altura = 0
	peso = 0
	nombre = 'Defecto'

	def __init__(self):
		self.altura= 1.77
		self.peso = 70
		self.nombre = 'Juan Sebastian'

	def dormir(hora):
		print nombre+' esta durmiendo desde las '+hora

	def comer(self):
		self.peso = self.peso + 1

class Estudiante(Persona):
	codigo = 0
	creditoscursados = 0
	
	def agregarCreditos(self,creditos):
		self.creditoscursados = creditos


juan = Estudiante()
juan.comer()
print juan.nombre
