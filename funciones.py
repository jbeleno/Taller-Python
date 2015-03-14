def saludo(nombre):
	print "hola "+str(nombre)

def sumar(x,y=0):
	resultado = x+y
	return resultado

nombre = 'Juan'
saludo(nombre)
suma = sumar(5,5)
print suma
