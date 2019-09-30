from terminal import clear_terminal, timed_input
from random import randrange
#from time import sleep

DIMENSIONES_TABLERO = (20, 10) # dimensiones del tablero en formato (ancho, alto)
LONGITUD_MAXIMA = 4
DT = 0.2 # paso temporal (en segundos) entre iteraciones, si es mas chico la vibora va mas rapido
TECLAS_DIRECCIONES = ('w', 's', 'a', 'd') # tupla con las cuatro direcciones posibles en la forma (arriba, abajo, izquierda, derecha)
TECLA_PAUSA = 'p'
TECLA_SALIR = 'q'
SIMBOLO_VIBORA = '#'
SIMBOLO_FRUTA = '*'

def main():
    
    tablero = crear_tablero(DIMENSIONES_TABLERO)
    fruta, vibora, direccion = inicializar(DIMENSIONES_TABLERO, TECLAS_DIRECCIONES)
    
    p = False
    input_usuario = ''
    
    while len(vibora) < LONGITUD_MAXIMA and not salir(input_usuario, TECLA_SALIR):
        input_usuario = timed_input(DT)
        if not p:
            direccion = actualizar_direccion(input_usuario, direccion, TECLAS_DIRECCIONES)
            juego(vibora, fruta, direccion, TECLAS_DIRECCIONES, DIMENSIONES_TABLERO)
                
            if perdio(vibora, DIMENSIONES_TABLERO):
                break
            
            modificar_tablero(vibora, fruta, tablero)
            clear_terminal()
            imprimir_tablero(tablero, SIMBOLO_VIBORA, SIMBOLO_FRUTA)
            
        p = pausa(input_usuario, p, TECLA_PAUSA)
    
    imprimir_mensaje_final(len(vibora), LONGITUD_MAXIMA)

def main_sin_adiciones():
    '''Jugar a la viborita sin poder salir (salvo que se pierda) o poner pausa'''    
    tablero = crear_tablero(DIMENSIONES_TABLERO)
    fruta, vibora, direccion = inicializar(DIMENSIONES_TABLERO, TECLAS_DIRECCIONES)
    
    while len(vibora) < LONGITUD_MAXIMA:
        direccion = actualizar_direccion(timed_input(DT), direccion, TECLAS_DIRECCIONES)                        
        juego(vibora, fruta, direccion, TECLAS_DIRECCIONES, DIMENSIONES_TABLERO)
                
        if perdio(vibora, DIMENSIONES_TABLERO):
            break
            
        modificar_tablero(vibora, fruta, tablero)
        clear_terminal()
        imprimir_tablero(tablero, SIMBOLO_VIBORA, SIMBOLO_FRUTA)
            
    imprimir_mensaje_final(len(vibora), LONGITUD_MAXIMA)
    
def main_con_pausa_sin_salir():
    '''Jugar a la viborita sin poder salir salvo perdiendo, pero se puede poner pausa'''    
    tablero = crear_tablero(DIMENSIONES_TABLERO)
    fruta, vibora, direccion = inicializar(DIMENSIONES_TABLERO, TECLAS_DIRECCIONES)
    
    p = False
    
    while len(vibora) < LONGITUD_MAXIMA:
        if not p:
            input_usuario = timed_input(DT)
            direccion = actualizar_direccion(input_usuario, direccion, TECLAS_DIRECCIONES)                        
            juego(vibora, fruta, direccion, TECLAS_DIRECCIONES, DIMENSIONES_TABLERO)
                    
            if perdio(vibora, DIMENSIONES_TABLERO):
                break
                
            modificar_tablero(vibora, fruta, tablero)
            clear_terminal()
            imprimir_tablero(tablero, SIMBOLO_VIBORA, SIMBOLO_FRUTA)
        
        p = pausa(input_usuario, p, TECLA_PAUSA)
            
    imprimir_mensaje_final(len(vibora), LONGITUD_MAXIMA)

def juego(vibora, fruta, direccion, TECLAS_DIRECCIONES, DIMENSIONES_TABLERO):
    avanzar_cabeza(vibora, direccion, TECLAS_DIRECCIONES)
            
    if comio_fruta(vibora, fruta):
        reubicar_fruta(vibora, fruta, DIMENSIONES_TABLERO)
    else:
        avanzar_cola(vibora)

def perdio(vibora, DIMENSIONES_TABLERO):
    '''
    Devuelve True si el usuario perdio (ya sea porque se comio a si mismo o
    porque la vibora salio del tablero) y False en caso contrario
    '''
    return se_mordio(vibora) or salio_del_tablero(vibora, DIMENSIONES_TABLERO)

def avanzar_cabeza(vibora, direccion, teclas_direcciones):
    '''Dadas las coordenadas de la vibora, la dirección en la que se está moviendo y la tupla de posibles direcciones, alarga la vibora en la dirección del movimiento'''
    movimientos_posibles = ((-1, 0), (1, 0), (0, -1), (0, 1))
    indice_direccion = teclas_direcciones.index(direccion)
    movimiento = movimientos_posibles[indice_direccion]
    vibora.append((vibora[-1][0] + movimiento[0], vibora[-1][1] + movimiento[1]))

def avanzar_cola(vibora):
    '''Dada la lista que representa a la vibora, le borra el último elemento, lo que tiene el efecto de un avance de la cola de la vibora'''
    vibora.pop(0)    

def comio_fruta(vibora, fruta):
    '''Dadas las coordenadas de la cabeza de la vibora y de la fruta, devuelve True si la vibora se comió a la fruta o False en caso contrario'''
    return vibora[-1] == tuple(fruta)

def se_mordio(vibora):
    '''Dadas las coordenadas de la vibora, devuelve True si se mordio a si misma o False si no'''
    return vibora[-1] in vibora[:-1]

def reubicar_fruta(vibora, fruta, dimensiones_tablero):
    '''Dadas las coordenadas de la vibora y las dimensiones del tablero, ubica la fruta en algún lugar del tablero no ocupado por la vibora'''
    while True:
        candidata_a_fruta = []
        candidata_a_fruta.append(randrange(dimensiones_tablero[1]))
        candidata_a_fruta.append(randrange(dimensiones_tablero[0]))
        if candidata_a_fruta not in vibora:
            fruta[0:2] = candidata_a_fruta
            break
    

def actualizar_direccion(input_usuario, direccion_actual, teclas_direcciones):
    '''
    Dada una cadena de caracteres ingresada por el usuario, actualiza la 
    direccion en la que se mueve la vibora. Si la vibora se mueve en una dirección
    vertical solamente permite cambiar a una dirección horizontal y viceversa
    '''
    if direccion_actual in teclas_direcciones[0:2]:
        teclas_posibles = teclas_direcciones[2] + teclas_direcciones[3]
    else:
        teclas_posibles = teclas_direcciones[0] + teclas_direcciones[1]
    for c in input_usuario:
        if c in teclas_posibles:
            return c
    return direccion_actual

def pausa(input_usuario, pausa_activada, tecla_pausa):
    '''
    Función que recibe la cadena ingresada por el usuario y el estado actual
    del programa (en pausa o no como booleano, True o False). Si el usuario 
    apretó la tecla de pausa, devuelve False si el juego estaba en pausa o 
    True si no lo estaba
    '''
    for c in input_usuario:
        if c == tecla_pausa:
            return not pausa_activada
    return pausa_activada

def salir(input_usuario, tecla_salir):
    '''Función que recibe la entrada del usuario y devuelve True si el usuario 
    apretó la tecla para salir del juego o False en caso contrario'''
    return tecla_salir in input_usuario

def crear_tablero_contupla(ancho_tablero, alto_tablero):
    '''Dado un ancho y alto del tablero, devuelve una lista de listas llena de ceros, que representa al tablero vacío (sin vibora ni fruta)'''
    fila = []
    for i in range(ancho_tablero):
        fila.append(0)
    
    tablero_vacio = []
    for j in range(alto_tablero):
        tablero_vacio.append(tuple(fila))
    
    tablero_vacio = tuple(tablero_vacio)
    tablero = [list(x) for x in tablero_vacio]
    return tablero


def crear_tablero_sintupla(ancho_tablero, alto_tablero):
    '''Dado un ancho y alto del tablero, devuelve una lista de listas llena de ceros, que representa al tablero vacío (sin vibora ni fruta)'''
    fila = []
    for i in range(ancho_tablero):
        fila.append(0)
    
    tablero_vacio = []
    for j in range(alto_tablero):
        tablero_vacio.append(fila)
    
    return tablero_vacio

def crear_tablero(dimensiones_tablero):
    '''Dado un ancho y alto del tablero, devuelve una lista de listas llena de 
    ceros, que representa al tablero vacío (sin vibora ni fruta)'''
    tablero_vacio = []
    for j in range(dimensiones_tablero[1]):    
        fila = []
        for i in range(dimensiones_tablero[0]):
            fila.append(0)
        tablero_vacio.append(fila)

    return tablero_vacio

def crear_tablero_fila(dimensiones_tablero):
    '''Dado un ancho y alto del tablero, devuelve una lista de listas llena de 
    ceros, que representa al tablero vacío (sin vibora ni fruta)'''
    tablero_vacio = []
    fila = []
    for i in range(dimensiones_tablero[0]):
        fila.append(0)
    
    for j in range(dimensiones_tablero[1]):
        tablero_vacio.append(fila)

    return tablero_vacio


def inicializar(dimensiones_tablero, teclas_direcciones):
    '''
    Dadas las dimensiones del tablero y las direcciones posibles, devuelve 
    la posicion inicial de la vibora (en el centro del tablero), la posición 
    inicial de la fruta (en una posición aleatoria distinta del centro del tablero)
    y la dirección inicial en la que se mueve la vibora (que es aleatoria)'''
    
    fruta = []
    fruta.append(randrange(dimensiones_tablero[1]))
    fruta.append(randrange(dimensiones_tablero[0]))
    
    vibora = []
    vibora.append((int(dimensiones_tablero[1]/2), int(dimensiones_tablero[0]/2)))
    
    if tuple(fruta) in vibora:
        fruta[0] += 1 # corro la fruta para que no coincida con la vibora inicialmente

    direccion = teclas_direcciones[randrange(4)] # inicialmente va en una direccion aleatoria
    
    return fruta, vibora, direccion

def modificar_tablero(vibora, fruta, tablero):
    '''
    Modifica la lista de listas tablero a partir de las coordenadas de la vibora
    y la posicion de la fruta. La posición en la cual se encuentra la fruta se
    representa con un número 2, las posiciones en las cuales se encuentra la vibora
    se representan con un número 1, y las restantes con un cero
    '''
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            tablero[i][j] = int([i, j] == fruta) * 2
        for i, j in vibora:
            tablero[i][j] = 1
            
def imprimir_tablero(tablero, simbolo_vibora, simbolo_fruta):
    '''Imprime el tablero en la pantalla'''
    alto_tablero = len(tablero)
    ancho_tablero = len(tablero[0])
    for i in range(alto_tablero):
        if i == 0:
            print('_' * (ancho_tablero + 1))
        for j in range(ancho_tablero):
            if j == 0:
                print('|', end = '')
            if j < ancho_tablero - 1:
                if tablero[i][j] == 0:
                    print(' ', end = '')
                elif tablero[i][j] == 1:
                    print(simbolo_vibora, end = '')
                elif tablero[i][j] == 2:
                    print(simbolo_fruta, end = '')
            else:
                if tablero[i][j] == 0:
                    print(' |')
                elif tablero[i][j] == 1:
                    print(simbolo_vibora + '|')
                elif tablero[i][j] == 2:
                    print(simbolo_fruta + '|') 
        if i == alto_tablero - 1:
            print('¯' * (ancho_tablero + 1))
            
def imprimir_mensaje_final(longitud_vibora, longitud_maxima):
    '''Imprime el mensaje final al usuario'''
    if longitud_vibora == longitud_maxima:
        print('Felicitaciones !')
    else:
        print('Buena suerte en el próximo intento.')
        
def salio_del_tablero(vibora, dimensiones_tablero):
    '''Dadas las coordenadas de la cabeza de la vibora y las dimensiones del tablero, devuelve True si la vibora salio del tablero o False en caso contrario'''
    return vibora[-1][0] < 0 or vibora[-1][0] >= dimensiones_tablero[1] or vibora[-1][1] < 0 or vibora[-1][1] >= dimensiones_tablero[0]

assert TECLA_PAUSA not in TECLAS_DIRECCIONES, "La tecla de pausa no puede coincidir con alguna de las teclas que mueven a la vibora."
assert TECLA_SALIR not in TECLAS_DIRECCIONES, "La tecla para salir del juego no puede coincidir con alguna de las teclas que mueven a la vibora."
assert TECLA_PAUSA != TECLA_SALIR, "La tecla para poner pausa no puede coincidir con la tecla para salir del juego."
assert LONGITUD_MAXIMA > 1, "La longitud máxima de la vibora debe ser al menos 2."
assert DT > 0, "El intervalo temporal debe ser positivo."
assert type(LONGITUD_MAXIMA) is int, "La longitud maxima (ganadora) de la vibora debe ser un entero."
assert len(TECLA_SALIR) == 1, "La cadena que representa la tecla para salir del juego debe tener longitud 1."
assert len(TECLA_PAUSA) == 1, "La cadena que representa la tecla para poner o sacar la pausa debe tener longitud 1."
assert len(TECLAS_DIRECCIONES) == 4, "La tupla que contiene las teclas para mover a la vibora debe tener longitud 4."
assert type(TECLA_SALIR) is str, "La variable TECLA_SALIR debe ser una cadena."
assert type(TECLA_PAUSA) is str, "La variable TECLA_PAUSA debe ser una cadena."
assert type(SIMBOLO_VIBORA) is str, "La variable SIMBOLO_VIBORA debe ser una cadena."
assert type(SIMBOLO_FRUTA) is str, "La variable SIMBOLO_FRUTA debe ser una cadena."
assert len(SIMBOLO_VIBORA) == 1, "La cadena que representa el símbolo de la vibora debe tener longitud 1."
assert len(SIMBOLO_FRUTA) == 1, "La cadena que representa el símbolo de la fruta debe tener longitud 1."
assert SIMBOLO_VIBORA != SIMBOLO_FRUTA, "Los símbolos de la víbora y de la fruta deben ser distintos."
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
