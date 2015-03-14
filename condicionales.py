condicion = True
condicion2 = False

#operadores logicos: and, or, not

if condicion:
	if condicion2 == True:
		print 'Condicion 1 y 2 positivas'
	else:
		print 'Condicion 1 positiva y condicion 2 falsa'
else:
	if condicion2:
		print 'La condicion 1 es falsa y condicion 2 es positiva'
	else:
		print 'Ambas condiciones son falsas'
