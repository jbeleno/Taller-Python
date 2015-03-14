lista = ['Juan', 'Sebastian', 22, 1.77]
lista2 = ['Daira', 'Carolina', 23, 1.72]
#print len(lista)
listaf = lista + lista2

if 22 in listaf:
	print 'Si'
else:
	print 'No'

for elemento in listaf:
	print elemento

print listaf[-1]
