x = 11
y = 2

resultado = x+y
print ("Suma: "+str(resultado))

resultado = x-y
print ('Resta: '+str(resultado))

resultado = x*y
print ('Multiplicacion: '+str(resultado))

#En python 2.* es necesario castear
resultado2 = x/float(y)
print ('division con decimales: '+str(resultado2))

#division entera
resultado = x//y
print ('division entera: '+str(resultado))

resultado = x%y
print ('modulo: '+str(resultado))

#exponentes
resultado = x**y
print ('exponente: '+str(resultado))
