#!/usr/bin/python
from time import time



def tam(num):
	return len(str(num))

def mult(u,v):
	n = max(tam(u),tam(v))
	if(n < 5 ):
		return u*v
	else:
		s = n / 2
		w = u / (10**s)
		x = u % (10**s)
		y = v / (10**s)
		z = v % (10**s)
		return (mult(w,y)*(10**(2*s))) + (mult(w,z)+mult(x,y))*(10**s) + mult(x,z)


def writeFile(fTime):
	archivo = open("datos.txt", "r+")
	contenido = archivo.read()
	final_de_archivo = archivo.tell()	 
	archivo.write(fTime+" "+str(TAM)+"\n")
	archivo.seek(final_de_archivo)
	archivo.close()


u = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
TAM = tam(u)
init_time = time()
mult(u,u)
final_time = time()
e_time = final_time - init_time
str_time = str("%.20f" % e_time)
writeFile(str_time)
print str_time

