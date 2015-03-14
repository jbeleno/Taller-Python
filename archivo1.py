def crearArchivo():
	archivo = open('datos.txt','w') #sobreescribir
	archivo.close()

def escribirArchivo():
	archivo = open('datos.txt', 'a') #append
	archivo.write("Juan Sebastian\n")
	archivo.write("jsbeleno@gmail.com\n")
	archivo.close()

def leerArchivo():
	archivo = open('datos.txt','r')
	linea = archivo.readline()
	while linea !="":
		print linea
		linea = archivo.readline()
	archivo.close()

#crearArchivo()
escribirArchivo()
leerArchivo()
