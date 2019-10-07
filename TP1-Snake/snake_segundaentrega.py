from terminal import clear_terminal, timed_input
from random import randrange

DIMENSIONES_TABLERO = (20, 10) # dimensiones del tablero en formato (ancho, alto)
LONGITUD_MAXIMA = 10 # longitud maxima de la vibora (si llega a esa longitud termina el juego y el usuario gana)
DT = 0.2 # paso temporal (en segundos) entre iteraciones, si es mas chico la vibora va mas rapido
TECLAS_DIRECCIONES = ('w', 's', 'a', 'd') # tupla con las cuatro direcciones posibles en la forma (arriba, abajo, izquierda, derecha)
SIMBOLO_VIBORA = '#'
SIMBOLO_FRUTA = '*'

def main():
    '''
    Flujo principal del juego snake. La vibora se mueve hacia 
    arriba, abajo, izquierda o derecha usando cuatro teclas del teclado, 
    especificadas en TECLAS_DIRECCIONES. Hay una fruta en la zona de juego 
    y cuando la vibora la come, la fruta aparece en otra posición y la longitud
    de la vibora se incrementa en una unidad. El juego termina cuando la longitud 
    de la vibora alcanza el valor prefijado LONGITUD_MAXIMA (en cuyo caso 
    el usuario gana), o si la vibora se come a si misma o sale del tablero, 
    en cuyo caso el usuario pierde.
    '''
    
    fruta, vibora, direccion = inicializar(DIMENSIONES_TABLERO, TECLAS_DIRECCIONES)
    
    while len(vibora) < LONGITUD_MAXIMA:

        direccion = actualizar_direccion(timed_input(DT), direccion, TECLAS_DIRECCIONES)                        
        juego(vibora, fruta, direccion, TECLAS_DIRECCIONES, DIMENSIONES_TABLERO)
                
        if perdio(vibora, DIMENSIONES_TABLERO):
            break
            
        modificar_tablero(vibora, fruta, tablero)

        clear_terminal()
        imprimir_tablero(vibora, fruta, DIMENSIONES_TABLERO, simbolo_vibora, simbolo_fruta)
        imprimir_comandos(TECLAS_DIRECCIONES)
        imprimir_avance(len(vibora), LONGITUD_MAXIMA)

    imprimir_mensaje_final(len(vibora), LONGITUD_MAXIMA)

def crear_tablero(dimensiones_tablero):
    '''Dado un ancho y alto del tablero, devuelve una lista de listas llena de 
    ceros, que representa al tablero vacío (sin vibora ni fruta).
    '''
    tablero_vacio = []
    for j in range(dimensiones_tablero[1]):    
        fila = []
        for i in range(dimensiones_tablero[0]):
            fila.append(0)
        tablero_vacio.append(fila)

    return tablero_vacio


def inicializar(dimensiones_tablero, teclas_direcciones):
    '''
    Dadas las dimensiones del tablero y los caracteres utilizados para mover a la vibora, devuelve 
    la posicion inicial de la vibora (en el centro del tablero), la posición 
    inicial de la fruta (en una posición aleatoria distinta del centro del tablero)
    y la dirección inicial en la que se mueve la vibora (que es aleatoria).
    '''

    fruta = []
    fruta.append(randrange(dimensiones_tablero[1]))
    fruta.append(randrange(dimensiones_tablero[0]))
    
    vibora = []
    vibora.append((int(dimensiones_tablero[1]/2), int(dimensiones_tablero[0]/2)))
    
    if tuple(fruta) in vibora:
        fruta[0] += 1 # corro la fruta para que no coincida con la vibora inicialmente

    direccion = teclas_direcciones[randrange(4)]
    
    return fruta, vibora, direccion

def actualizar_direccion(input_usuario, direccion_actual, teclas_direcciones):
    '''
    Dada una cadena de caracteres ingresada por el usuario, actualiza la 
    direccion en la que se mueve la vibora, tomando el primer caracter 
    de la cadena ingresada que coincida con uno de los caracteres 
    que se utilizan para mover a la vibora. Si la vibora se mueve en una dirección
    vertical solamente permite cambiar a una dirección horizontal y viceversa.
    '''
    if direccion_actual in teclas_direcciones[0:2]:
        teclas_posibles = teclas_direcciones[2] + teclas_direcciones[3]
    else:
        teclas_posibles = teclas_direcciones[0] + teclas_direcciones[1]
    for c in input_usuario:
        if c in teclas_posibles:
            return c
    return direccion_actual

def juego(vibora, fruta, direccion, TECLAS_DIRECCIONES, DIMENSIONES_TABLERO):
    '''A partir de la dirección en que se mueve la vibora, sus coordenadas 
    y las de la fruta, se lleva adelante el movimiento de la vibora y la reubicación 
    de la fruta si la misma fue comida por la vibora 
    (en cuyo caso la vibora aumenta su longitud en una unidad)
    '''
    avanzar_cabeza(vibora, direccion, TECLAS_DIRECCIONES)
            
    if comio_fruta(vibora, fruta):
        reubicar_fruta(vibora, fruta, DIMENSIONES_TABLERO)
    else:
        avanzar_cola(vibora)

def avanzar_cabeza(vibora, direccion, teclas_direcciones):
    '''Dadas las coordenadas de la vibora, la dirección en la que se está moviendo 
    y la tupla que contiene las teclas para mover a la vibora, 
    alarga a la vibora en la dirección del movimiento.
    '''
    movimientos_posibles = ((-1, 0), (1, 0), (0, -1), (0, 1))
    indice_direccion = teclas_direcciones.index(direccion)
    movimiento = movimientos_posibles[indice_direccion]
    vibora.append((vibora[-1][0] + movimiento[0], vibora[-1][1] + movimiento[1]))

def avanzar_cola(vibora):
    '''Le saca el ultimo elemento a la lista que representa a la vibora, lo que tiene el efecto de un avance de la cola de la vibora.'''
    vibora.pop(0)    

def comio_fruta(vibora, fruta):
    '''Dadas las coordenadas de la vibora y de la fruta, devuelve True si la vibora se comió a la fruta o False en caso contrario'''
    return vibora[-1] == tuple(fruta)

def reubicar_fruta(vibora, fruta, dimensiones_tablero):
    '''Dadas las coordenadas de la vibora y las dimensiones del tablero,
    ubica la fruta en algún lugar del tablero no ocupado por la vibora.
    '''
    while True:
        candidata_a_fruta = []
        candidata_a_fruta.append(randrange(dimensiones_tablero[1]))
        candidata_a_fruta.append(randrange(dimensiones_tablero[0]))
        if tuple(candidata_a_fruta) not in vibora:
            fruta[0:2] = candidata_a_fruta
            break

def perdio(vibora, DIMENSIONES_TABLERO):
    '''Devuelve True si el usuario perdio (ya sea porque se comio a si mismo o
    porque la vibora salio del tablero) y False en caso contrario.
    '''
    return se_mordio(vibora) or salio_del_tablero(vibora, DIMENSIONES_TABLERO)

def se_mordio(vibora):
    '''Dadas las coordenadas de la vibora, devuelve True si se mordio a si misma o False si no'''
    return vibora[-1] in vibora[:-1]

def salio_del_tablero(vibora, dimensiones_tablero):
    '''Dadas las coordenadas de la vibora y las dimensiones del tablero, 
    devuelve True si la vibora salio del tablero o False en caso contrario
    '''
    cabeza_vibora = vibora[-1]
    return -1 in cabeza_vibora or cabeza_vibora[0] == dimensiones_tablero[1] or cabeza_vibora[1] == dimensiones_tablero[0]
    

def modificar_tablero(vibora, fruta, tablero):
    '''
    Modifica la lista de listas tablero a partir de las coordenadas de la vibora
    y la posicion de la fruta. La posición en la cual se encuentra la fruta se
    representa con un número 2, las posiciones en las cuales se encuentra la vibora
    se representan con un número 1, y las restantes con un 0.
    '''
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            tablero[i][j] = int([i, j] == fruta) * 2
        for i, j in vibora:
            tablero[i][j] = 1

def imprimir_tablero(vibora, fruta, DIMENSIONES_TABLERO, simbolo_vibora, simbolo_fruta):
    '''
    Imprime el tablero en la pantalla. Donde no hay vibora ni fruta imprime un espacio,
    y donde hay vibora o fruta imprime el caracter correspondiente.
    '''
    alto_tablero = DIMENSIONES_TABLERO[1]
    ancho_tablero = DIMENSIONES_TABLERO[0]
    simbolos_imprimir = (' ', simbolo_vibora, simbolo_fruta)
    
    tablero = []
    for j in range(alto_tablero):    
        fila = []
        for i in range(ancho_tablero):
            fila.append(0)
        tablero.append(fila)
    
    tablero[fruta[0]][fruta[1]] = 2
    
    for i, j in vibora:
        tablero[i][j] = 1
    
    for i in range(alto_tablero):
        if i == 0:
            print('_' * (ancho_tablero + 2))
        for j in range(ancho_tablero):
            if j == 0:
                print('|', end = '')
            if j < ancho_tablero - 1:
                print(simbolos_imprimir[tablero[i][j]], end = '')
            else:
                print(simbolos_imprimir[tablero[i][j]] + '|')
        if i == alto_tablero - 1:
            print('¯' * (ancho_tablero + 2))

def imprimir_comandos(teclas_direcciones):
    '''Imprime las teclas que se usan para mover a la vibora.'''
    direcciones = ('arriba', 'abajo', 'izquierda', 'derecha')
    print('Comandos:')
    print()
    for i in range(len(teclas_direcciones)):
        print(str(direcciones[i]) + ': ' + str(teclas_direcciones[i]))
    print()

def imprimir_avance(longitud_vibora, longitud_maxima):
    '''Imprime el estado de avance en el juego (cuantas frutas comió y cuántas faltan para ganar). Si el usuario ganó, lo felicita.'''
    frutas_faltan = longitud_maxima - longitud_vibora
    print('Comiste ' + str(longitud_vibora - 1) + ' fruta', end = '')
    if longitud_vibora != 2:
        print('s', end = '')
    
    print(', ', end = '')

    if frutas_faltan == 0:
        print('ganaste.')
    else:
        print('te falta', end = '')
        if frutas_faltan != 1:
            print('n', end = '')
        print(' ' + str(frutas_faltan) + ' para ganar.')


def imprimir_mensaje_final(longitud_vibora, longitud_maxima):
    '''Imprime el mensaje final al usuario'''
    print() # para dejar un espacio
    if longitud_vibora == longitud_maxima:
        print('Felicitaciones!')
    else:
        print('Buena suerte en el próximo intento.')

main()
