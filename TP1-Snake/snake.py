from terminal import clear_terminal, timed_input
from random import randrange
#from time import sleep

ANCHO_TABLERO = 20 # ancho del tablero, M
ALTO_TABLERO = 10  # alto del tablero, N
LONGITUD_MAXIMA = 8
DT = 0.2 # paso temporal (en segundos) entre iteraciones, si es mas chico la vibora va mas rapido
TECLAS_DIRECCIONES = ('w', 's', 'a', 'd') # tupla con las cuatro direcciones posibles en la forma (arriba, abajo, izquierda, derecha)
TECLA_PAUSA = 'p'
TECLA_SALIR = 'q'

def main():
    
    tablero, fruta, vibora = inicializar(ANCHO_TABLERO, ALTO_TABLERO)
    
    direccion = TECLAS_DIRECCIONES[randrange(4)] # inicialmente va en una direccion aleatoria
    
    p = False
    while len(vibora[0]) < LONGITUD_MAXIMA:
        input_usuario = tuple(timed_input(DT))
        if not p:
            direccion = actualizar_direccion(input_usuario, direccion, TECLAS_DIRECCIONES)
            
            comio_fruta = actualizar_estado(vibora, direccion, fruta, TECLAS_DIRECCIONES)
                    
            if comio_fruta:
                fruta = reubicar_fruta(vibora, ANCHO_TABLERO, ALTO_TABLERO)
            
            if se_mordio(vibora) or salir(input_usuario, TECLA_SALIR) or salio_del_tablero(vibora, ANCHO_TABLERO, ALTO_TABLERO): # quit
                break
            
            modificar_tablero(fruta, vibora, tablero)
            
            clear_terminal()
            imprimir_tablero(tablero)
            
        p = pausa(input_usuario, p, TECLA_PAUSA)
    
    imprimir_mensaje_final(len(vibora[0]), LONGITUD_MAXIMA)


def actualizar_estado(vibora, direccion, fruta, teclas_direcciones):
    '''Dadas las coordenadas de la vibora y de la fruta y la dirección en la que se está moviendo la vibora, devuelve dos booleanos, uno que indica si la vibora comio una fruta en ese movimiento, y otro que indica si se mordio a si misma'''
    if direccion == teclas_direcciones[0]:
        vibora[0].append(vibora[0][len(vibora[0])-1] - 1)
        vibora[1].append(vibora[1][len(vibora[1])-1])
    if direccion == teclas_direcciones[1]:
        vibora[0].append(vibora[0][len(vibora[0])-1] + 1)
        vibora[1].append(vibora[1][len(vibora[1])-1])
    if direccion == teclas_direcciones[2]:
        vibora[0].append(vibora[0][len(vibora[0])-1])
        vibora[1].append(vibora[1][len(vibora[1])-1] - 1)
    if direccion == teclas_direcciones[3]:
        vibora[0].append(vibora[0][len(vibora[0])-1])
        vibora[1].append(vibora[1][len(vibora[1])-1] + 1)
    if vibora[0][len(vibora[0])-1] != fruta[0] or vibora[1][len(vibora[1])-1] != fruta[1]:
        vibora[0].pop(0)
        vibora[1].pop(0)
        comio_fruta = False
    else:
        comio_fruta = True
    return comio_fruta
    

def se_mordio(vibora):
    '''Dadas las coordenadas de la vibora, devuelve True si se mordio a si misma o False si no'''
    for k in range(len(vibora[0])-1):
        if vibora[0][k] == vibora[0][len(vibora[0])-1] and vibora[1][k] == vibora[1][len(vibora[0])-1]:
            return True
    return False

def reubicar_fruta(vibora, ancho_tablero, alto_tablero):
    '''Dadas las coordenadas de la vibora y las dimensiones del tablero, ubica la fruta en algún lugar del tablero no ocupado por la vibora'''
    while True:
        fruta = []
        fruta.append(randrange(alto_tablero))
        fruta.append(randrange(ancho_tablero))
        if fruta[0] not in vibora[0] or fruta[1] not in vibora[1]:
            return fruta
    
    #return vibora[0], vibora[1]

def actualizar_direccion(input_usuario, direccion_actual, teclas_direcciones):
    '''Dada una cadena de caracteres ingresada por el usuario, actualiza la direccion en la que se mueve la vibora'''
    if direccion_actual == teclas_direcciones[0] or direccion_actual == teclas_direcciones[1]:
        teclas_posibles = teclas_direcciones[2] + teclas_direcciones[3]
    else:
        teclas_posibles = teclas_direcciones[0] + teclas_direcciones[1]
    for c in input_usuario:
        if c in teclas_posibles:
            return c
    return direccion_actual

def pausa(input_usuario, pausa_activada, tecla_pausa):
    '''Función que recibe la cadena ingresada por el usuario y el estado actual del programa (en pausa o no como booleano, True o False). Si el usuario apretó la tecla de pausa, devuelve False si el juego estaba en pausa o True si no lo estaba'''
    for c in input_usuario:
        if c == tecla_pausa:
            return not pausa_activada
    return pausa_activada

def salir(input_usuario, tecla_salir):
    '''Función que recibe la entrada del usuario y devuelve True si el usuario apretó la tecla para salir del juego o False en caso contrario'''
    if tecla_salir in input_usuario:
        return True
    return False

def crear_tablero(ancho_tablero, alto_tablero):
    '''Dado un ancho y alto del tablero, devuelve una tupla de tuplas llena de ceros, que representa al tablero vacío (sin vibora ni fruta)'''
    fila = []
    for i in range(ancho_tablero):
        fila.append(0)
    
    tablero_vacio = []
    for j in range(alto_tablero):
        tablero_vacio.append(tuple(fila))
    
    tablero_vacio = tuple(tablero_vacio)
    tablero = [list(x) for x in tablero_vacio]
    return tablero

def inicializar(ancho_tablero, alto_tablero):
    '''Dadas las dimensiones del tablero, devuelve una lista de listas con ceros en todas las entradas que representa al tablero vacio, la posicion inicial de la vibora (en el centro del tablero) y la posición inicial de la fruta (en una posición aleatoria distinta del centro del tablero)'''
    tablero = crear_tablero(ancho_tablero, alto_tablero)
    
    fruta = []
    fruta.append(randrange(alto_tablero))
    fruta.append(randrange(ancho_tablero))
    
    # coloco inicialmente a la vibora en el centro del tablero
    vibora = []
    vibora.append([int(alto_tablero/2)])
    vibora.append([int(ancho_tablero/2)])
    
    if fruta[0] == vibora[0][0] and fruta[1] == vibora[1][0]: # en el caso de que la fruta caiga justo en la posicion inicial de la vibora, o sea en el centro del tablero
        fruta[0] += 1 # corro la fruta para que no coincida con la vibora inicialmente
    
    return tablero, fruta, vibora

def modificar_tablero(fruta, vibora, tablero):
    '''Modifica la lista tablero a partir de las coordenadas de la vibora y la posicion de la fruta'''
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if i == fruta[0] and j == fruta[1]:
                tablero[i][j] = 2
            else:
                tablero[i][j] = 0
        for k in range(len(vibora[0])):
            tablero[vibora[0][k]][vibora[1][k]] = 1
            
def imprimir_tablero(tablero):
    '''Imprime el tablero en la pantalla'''
    ancho_tablero = len(tablero[0])
    for i in range(len(tablero)):
        if i == 0:
            print('_' * (ancho_tablero + 1))
        for j in range(len(tablero[0])):
            if j == 0:
                print('|', end = '')
            if j < len(tablero[0]) - 1:
                if tablero[i][j] == 0:
                    print(' ', end = '')
                elif tablero[i][j] == 1:
                    print('#', end = '')
                elif tablero[i][j] == 2:
                    print('*', end = '')
            else:
                if tablero[i][j] == 0:
                    print(' |')
                elif tablero[i][j] == 1:
                    print('#|')
                elif tablero[i][j] == 2:
                    print('*|') 
        if i == len(tablero)-1:
            print('¯' * (ancho_tablero + 1))
            
def imprimir_mensaje_final(longitud_vibora, longitud_maxima):
    '''Imprime el mensaje final al usuario'''
    if longitud_vibora == longitud_maxima:
        print('Felicitaciones !')
    else:
        print('Seguí participando')
        
def salio_del_tablero(vibora, ancho_tablero, alto_tablero):
    '''Dadas las coordenadas de la vibora y las dimensiones del tablero, devuelve True si la vibora salio del tablero o False en caso contrario'''
    if vibora[0][len(vibora[0])-1] < 0 or vibora[0][len(vibora[0])-1] >= alto_tablero or vibora[1][len(vibora[0])-1] < 0 or vibora[1][len(vibora[0])-1] >= ancho_tablero:
        return True
    return False

assert TECLA_PAUSA not in TECLAS_DIRECCIONES, "La tecla de pausa no puede coincidir con alguna de las teclas que mueven a la vibora."
assert TECLA_SALIR not in TECLAS_DIRECCIONES, "La tecla para salir del juego no puede coincidir con alguna de las teclas que mueven a la vibora."
assert TECLA_PAUSA != TECLA_SALIR, "La tecla para poner pausa no puede coincidir con la tecla para salir del juego."
assert LONGITUD_MAXIMA > 1, "La longitud máxima de la vibora debe ser al menos 2."
assert type(ANCHO_TABLERO) is int, "El ancho del tablero debe ser un entero."
assert type(ALTO_TABLERO) is int, "La altura del tablero debe ser un entero."
assert ANCHO_TABLERO > 2, "El ancho del tablero debe ser mayor a 2."
assert ALTO_TABLERO > 2, "La altura del tablero debe ser mayor a 2."
assert DT > 0, "El intervalo temporal debe ser positivo."
assert type(LONGITUD_MAXIMA) is int, "La longitud maxima (ganadora) de la vibora debe ser un entero."
assert len(TECLA_SALIR) == 1, "La cadena que representa la tecla para salir del juego debe tener longitud 1."
assert len(TECLA_PAUSA) == 1, "La cadena que representa la tecla para poner o sacar la pausa debe tener longitud 1."
assert len(TECLAS_DIRECCIONES) == 4, "La tupla que contiene las teclas para mover a la vibora debe tener longitud 4."
assert type(TECLA_SALIR) is str, "La variable TECLA_SALIR debe ser una cadena."
assert type(TECLA_PAUSA) is str, "La variable TECLA_PAUSA debe ser una cadena."
assert type(TECLAS_DIRECCIONES) is tuple, "La variable TECLAS_DIRECCIONES debe ser una tupla."
assert type(TECLAS_DIRECCIONES[0]) is str, "Los elementos de TECLAS_DIRECCIONES deben ser cadenas de longitud 1."
assert type(TECLAS_DIRECCIONES[1]) is str, "Los elementos de TECLAS_DIRECCIONES deben ser cadenas de longitud 1."
assert type(TECLAS_DIRECCIONES[2]) is str, "Los elementos de TECLAS_DIRECCIONES deben ser cadenas de longitud 1."
assert type(TECLAS_DIRECCIONES[3]) is str, "Los elementos de TECLAS_DIRECCIONES deben ser cadenas de longitud 1."
assert len(TECLAS_DIRECCIONES[0]) == 1, "Los elementos de TECLAS_DIRECCIONES deben ser cadenas de longitud 1."
assert len(TECLAS_DIRECCIONES[1]) == 1, "Los elementos de TECLAS_DIRECCIONES deben ser cadenas de longitud 1."
assert len(TECLAS_DIRECCIONES[2]) == 1, "Los elementos de TECLAS_DIRECCIONES deben ser cadenas de longitud 1."
assert len(TECLAS_DIRECCIONES[3]) == 1, "Los elementos de TECLAS_DIRECCIONES deben ser cadenas de longitud 1."
assert TECLAS_DIRECCIONES[0] != TECLAS_DIRECCIONES[1], "Los elementos de TECLAS_DIRECCIONES deben ser todos distintos entre si."
assert TECLAS_DIRECCIONES[0] != TECLAS_DIRECCIONES[2], "Los elementos de TECLAS_DIRECCIONES deben ser todos distintos entre si."
assert TECLAS_DIRECCIONES[0] != TECLAS_DIRECCIONES[3], "Los elementos de TECLAS_DIRECCIONES deben ser todos distintos entre si."
assert TECLAS_DIRECCIONES[1] != TECLAS_DIRECCIONES[2], "Los elementos de TECLAS_DIRECCIONES deben ser todos distintos entre si."
assert TECLAS_DIRECCIONES[1] != TECLAS_DIRECCIONES[3], "Los elementos de TECLAS_DIRECCIONES deben ser todos distintos entre si."
assert TECLAS_DIRECCIONES[2] != TECLAS_DIRECCIONES[3], "Los elementos de TECLAS_DIRECCIONES deben ser todos distintos entre si."

main()
