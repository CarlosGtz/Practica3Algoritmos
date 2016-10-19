#!/usr/bin/python
from time import time
import random

A = []
TAM = 13000

def llenaArreglo(p):
	for i in range(TAM):
		p.append(random.randint(1, 500000))

def writeFile(fTime):
	archivo = open("datos.txt", "r+")
	contenido = archivo.read()
	final_de_archivo = archivo.tell()	 
	archivo.write(fTime+" "+str(TAM)+"\n")
	archivo.seek(final_de_archivo)
	archivo.close()

def Maximo(ini, fin, maxi):
	max_aux = maxi
	if(ini == fin):
		max_aux = A[ini]
	else:
		mitad =  int((ini+fin)/2)
		Maximo(ini,mitad,maxi)
		Maximo(mitad+1,fin,max_aux)
		if(max_aux>maxi):
			maxi = max_aux


llenaArreglo(A)
init_time = time()
Maximo(0,TAM-1,0)
final_time = time()
e_time = final_time - init_time
str_time = str("%.20f" % e_time)
writeFile(str_time)

print "Time: %.20f" % e_time