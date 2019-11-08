from mapa2 import Mapa,Coord
from random import randrange

def generar_laberinto(filas, columnas):
    """Generar un laberinto.

    Argumentos:
        filas, columnas (int): Tamaño del mapa

    Devuelve:
        Mapa: un mapa nuevo con celdas bloqueadas formando un laberinto
              aleatorio
    """
    visitadas=[]
    laberinto=Mapa(filas,columnas)
    impares=[]
    for i in range(1,laberinto.dimension()[0],2):
    	for j in range(1,laberinto.dimension()[1],2):
    		impares.append((i,j))
    i,j=laberinto.origen
    print(impares)
    visitadas.append((i,j))
    laberinto.desbloquear(laberinto.origen)
    while not mismos_elementos(visitadas,impares):
    	df=randrange(-2,3,2)
    	dc=randrange(-2,3,2)
    	if laberinto.es_coord_valida((i+df,j+dc)) and (i+df,j+dc) not in visitadas:
    		celda_del_medio=obtener_celda_del_medio(i,j,df,dc)
    		i+=df
    		j+=dc
    		print(i,j)
    		print(celda_del_medio)
    		laberinto.desbloquear((i,j))
    		laberinto.desbloquear(celda_del_medio)
    		visitadas.append((i,j))

    return laberinto 		





def mismos_elementos(visitadas,impares):
	'''Verifica si y se visitaron todas las celdas impares'''
	for celda in impares:
		if celda not in visitadas:
			return False
	return True		
    				
def obtener_celda_del_medio(i,j,df,dc):
	'''Halla la posicion entre dos celdas impares'''
	aux={2:1,0:0,-2:-1}
	i+=aux[df]
	j+=aux[dc]
	return i,j
			
