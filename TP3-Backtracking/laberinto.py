from mapa import Mapa, Coord
from random import randrange, choice
from pila import Pila

def generar_laberinto(filas, columnas):
    """Generar un laberinto.

    Argumentos:
        filas, columnas (int): Tamaño del mapa

    Devuelve:
        Mapa: un mapa nuevo con celdas bloqueadas formando un laberinto
              aleatorio
    """
    visitadas = []
    laberinto = Mapa(filas, columnas)
    impares = []
    camino = Pila()
    for i in range(1, laberinto.dimension()[0],2):
    	for j in range(1,laberinto.dimension()[1],2):
    		impares.append(Coord(i, j))
    actual = laberinto.origen()
    print(impares)
    visitadas.append(actual)
    laberinto.desbloquear(actual)

    while not mismos_elementos(visitadas, impares):
        vecinos = obtener_vecinos_impares(actual, laberinto)
        vecinos_no_visitados = filtrar_no_visitados(vecinos, visitadas)
        if len(vecinos_no_visitados) > 1:
            camino.apilar(actual)
        if vecinos_no_visitados:
            vecino = choice(vecinos_no_visitados)
            celda_del_medio = obtener_celda_del_medio(actual, vecino)
            actual = vecino
            print(actual)
            print(celda_del_medio)
            laberinto.desbloquear(actual)
            laberinto.desbloquear(celda_del_medio)
            visitadas.append(actual)
        else:
            while not camino.esta_vacia():
                candidata_a_nueva = camino.desapilar()
                if len(filtrar_no_visitados(obtener_vecinos_impares(candidata_a_nueva, laberinto), visitadas)) > 0:
                    actual = candidata_a_nueva
                    break
    return laberinto

def obtener_vecinos_impares(actual, mapa):
    '''
    Dada una coordenada en el mapa y el mapa, devuelve una lista
    con las coordenadas de los vecinos (considerando los que estan a dos celdas
    de distancia).
    '''
    vecinos = []
    movimientos_posibles = ((2, 0), (0, 2), (-2, 0), (0, -2))
    if actual == mapa.destino():
        return vecinos
    for movimiento in movimientos_posibles:
        df, dc = movimiento
        posible_vecino = actual.trasladar(df, dc)
        if mapa.es_coord_valida(posible_vecino):
            vecinos.append(posible_vecino)
    return vecinos

def filtrar_no_visitados(vecinos, visitadas):
    vecinos_no_visitados = []
    for vecino in vecinos:
        if vecino not in visitadas:
            vecinos_no_visitados.append(vecino)
    return vecinos_no_visitados

def mismos_elementos(visitadas, impares):
	'''Verifica si y se visitaron todas las celdas impares'''
	for celda in impares:
		if celda not in visitadas:
			return False
	return True

def obtener_celda_del_medio_vieja(i, j, df, dc):
    '''Halla la posicion entre dos celdas impares''' # la reescribí porque me parecía más clara así (sin pasar por el diccionario). Igual al final la termine reemplazando por una nueva (la dejo por si queremos volver a esta)
    i += int(df/2)
    j += int(dc/2)
    return i, j

def obtener_celda_del_medio(actual, vecino):
    '''Halla la posicion entre dos celdas impares'''
    return Coord(int((actual.fila + vecino.fila)/2), int((actual.columna + vecino.columna)/2))

def imprimir(laberinto):
    '''Imprime el laberinto en la terminal'''
    f, c = laberinto.dimension()
    for i in range(f):
        fin = ''
        for j in range(c):
            if j == c - 1:
                fin = None
            if laberinto.celda_bloqueada(Coord(i, j)):
                print(chr(9608), end = fin) # 9632 es el cuadrado
            else:
                print(' ', end = fin)
