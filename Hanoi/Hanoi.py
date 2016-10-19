#!/usr/bin/python
from time import time

TAM = int(input("FNumero de discos>>"))
	
def Hanoi(n, origen, auxiliar, destino):
	if n ==1 :
		print (str(origen) + " -> " + str(destino))
	else:
		Hanoi(n-1, origen, destino, auxiliar)
		print (str(origen) + " -> " + str(destino))
		Hanoi(n-1, auxiliar, origen, destino)

def writeFile(fTime):
	archivo = open("datos.txt", "r+")
	contenido = archivo.read()
	final_de_archivo = archivo.tell()	 
	archivo.write(fTime+" "+str(TAM)+"\n")
	archivo.seek(final_de_archivo)
	archivo.close()

init_time = time()

Hanoi(TAM,1,2,3)
final_time = time()
e_time = final_time - init_time
str_time = str("%.20f" % e_time)
writeFile(str_time)
print "Time: %.20f" % e_time

    
    
  