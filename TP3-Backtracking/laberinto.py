from mapa import Mapa, Coord
from random import choice
from pila import Pila

def generar_laberinto(filas, columnas):
    """Generar un laberinto.

    Argumentos:
        filas, columnas (int): Tamaño del mapa

    Devuelve:
        Mapa: un mapa nuevo con celdas bloqueadas formando un laberinto
              aleatorio
    """

    laberinto = Mapa(filas, columnas)

    laberinto.asignar_origen(Coord(1, 1))
    laberinto.asignar_destino(Coord(filas - 1 - filas % 2, columnas - 1 - columnas % 2))

    for coord in laberinto:
        laberinto.bloquear(coord)

    impares = todas_las_impares(laberinto)

    visitadas = []
    actual = laberinto.origen()
    visitadas.append(actual)
    laberinto.desbloquear(actual)

    posibles_candidatos = Pila()

    while not todos_contenidos(visitadas, impares):
        vecinos = vecinos_misma_paridad(actual, laberinto)
        vecinos_no_visitados = no_visitadas(vecinos, visitadas)
        if vecinos_no_visitados and actual != laberinto.destino():
            posibles_candidatos.apilar(actual)
            vecino = choice(vecinos_no_visitados)
            celda_del_medio = obtener_celda_del_medio(actual, vecino)
            actual = vecino
            laberinto.desbloquear(actual)
            laberinto.desbloquear(celda_del_medio)
            visitadas.append(actual)
        else:
            while not posibles_candidatos.esta_vacia():
                candidata_a_nueva = posibles_candidatos.desapilar()
                if no_visitadas(vecinos_misma_paridad(candidata_a_nueva, laberinto), visitadas):
                    actual = candidata_a_nueva
                    break
    return laberinto

def todas_las_impares(mapa):
    '''
    Dado un mapa, devuelve una tupla de coordenadas que contiene
    a todas las coordenadas impares.
    '''
    impares = []
    for i in range(1, mapa.dimension()[0],2):
    	for j in range(1, mapa.dimension()[1],2):
    		impares.append(Coord(i, j))
    return tuple(impares)

def vecinos_misma_paridad(actual, mapa):
    '''
    Dada una coordenada en el mapa y el mapa, devuelve una tupla
    con las coordenadas de los vecinos que están a dos celdas
    de distancia (de manera tal de conservar la paridad, es decir,
    si la coordenada es impar da los vecinos impares y si es par
    da los vecinos pares).
    '''
    vecinos = []
    movimientos_posibles = ((2, 0), (0, 2), (-2, 0), (0, -2))
    for movimiento in movimientos_posibles:
        df, dc = movimiento
        posible_vecino = actual.trasladar(df, dc)
        if mapa.es_coord_valida(posible_vecino):
            vecinos.append(posible_vecino)
    return tuple(vecinos)

def no_visitadas(coordenadas, visitadas):
    '''
    Recibe una tupla de coordenadas y una lista de coordenadas visitadas
    y devuelve una tupla con las coordenadas no visitadas.
    '''
    coord_no_visitadas = []
    for coord in coordenadas:
        if coord not in visitadas:
            coord_no_visitadas.append(coord)
    return tuple(coord_no_visitadas)

def todos_contenidos(s1, s2):
    '''
    Recibe dos secuencias y devuelve True si todos los elementos
    de la segunda están en la primera o False en caso contrario.
    '''
    for elemento in s2:
        if elemento not in s1:
            return False
    return True

def obtener_celda_del_medio(celda_1, celda_2):
    '''
    Recibe las coordenadas de dos celdas separadas en dos unidades y
    devuelve las coordenadas de la celda ubicada entre esas dos.
    '''
    return Coord(int((celda_1.fila + celda_2.fila)/2), int((celda_1.columna + celda_2.columna)/2))
