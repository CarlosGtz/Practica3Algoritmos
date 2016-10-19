#!/usr/bin/python
from time import time
import random

A = []
TAM = 2000000

def llenaArreglo(p):
	for i in range(TAM):
		p.append(random.randint(1, 500000000))

def writeFile(fTime):
	archivo = open("datos.txt", "r+")
	contenido = archivo.read()
	final_de_archivo = archivo.tell()	 
	archivo.write(fTime+" "+str(TAM)+"\n")
	archivo.seek(final_de_archivo)
	archivo.close()

def Pivote(a,prim,ult):
	pos = prim
	for i in range(prim,ult):
		if(a[i] < a[ult]):
			a[i],a[pos] = a[pos],a[i]
			pos+=1
	a[pos],a[ult] = a[ult],a[pos]
	return pos


def Quick(a, prim,ult):	
	if( prim < ult ):
		pos = Pivote(a,prim,ult)
		Quick(a,prim,pos-1)
		Quick(a,pos+1,ult)

llenaArreglo(A)
init_time = time()
Quick(A,0,len(A)-1)
final_time = time()
e_time = final_time - init_time
str_time = str("%.20f" % e_time)
writeFile(str_time)
print str_time
