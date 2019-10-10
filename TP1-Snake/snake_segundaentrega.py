from terminal import clear_terminal, timed_input
from random import randrange

ANCHO_TABLERO = 20
ALTO_TABLERO = 10
LONGITUD_MAXIMA = 10 # longitud maxima de la vibora (si llega a esa longitud termina el juego y el usuario gana)
DT = 0.2 # paso temporal (en segundos) entre iteraciones, si es mas chico la vibora va mas rapido
TECLAS_DIRECCIONES = ('w', 's', 'a', 'd') # tupla con las cuatro direcciones posibles en la forma (arriba, abajo, izquierda, derecha)
SIMBOLO_VIBORA = '#'
SIMBOLO_FRUTA = '*'

def main():
    '''
    Flujo principal del juego snake.
    '''
    
    vibora, fruta, direccion = estado_inicial()
    
    snake(vibora, fruta, direccion)

    imprimir_mensaje_final(len(vibora))


def snake(vibora, fruta, direccion):
    '''
    Funcion principal del juego snake. La vibora se mueve hacia 
    arriba, abajo, izquierda o derecha usando cuatro teclas del teclado, 
    especificadas en la constante global TECLAS_DIRECCIONES. 
    Hay una fruta en la zona de juego y cuando la vibora la come, la fruta 
    aparece en otra posición y la longitud de la vibora se incrementa en 
    una unidad. El juego termina cuando la longitud de la vibora alcanza el valor 
    prefijado en la constante global LONGITUD_MAXIMA (en cuyo caso 
    el usuario gana), o si la vibora se come a si misma o sale del tablero, 
    en cuyo caso el usuario pierde.
    '''
    while len(vibora) < LONGITUD_MAXIMA:

        direccion = actualizar_direccion(timed_input(DT), direccion)                        
        
        avanzar_cabeza(vibora, direccion)

        if comio_fruta(vibora, fruta):
            reubicar_fruta(vibora, fruta)
        else:
            avanzar_cola(vibora)

        if perdio(vibora):
            break
                
        clear_terminal()
        imprimir_tablero(vibora, fruta)
        imprimir_comandos()
        imprimir_avance(len(vibora))

def estado_inicial():
    '''
    Dadas las dimensiones del tablero y los caracteres utilizados para mover a la vibora
    (especificadas como constantes globales), devuelve 
    la posicion inicial de la vibora (en el centro del tablero), la posición 
    inicial de la fruta (en una posición aleatoria distinta del centro del tablero)
    y la dirección inicial en la que se mueve la vibora (que es aleatoria).
    '''

    vibora = crear_vibora()
    
    fruta = [0, 0]
    reubicar_fruta(vibora, fruta) # a posicion aleatoria

    direccion = TECLAS_DIRECCIONES[randrange(4)]
    
    return vibora, fruta, direccion
    
def crear_vibora():
    '''
    Devuelve una lista con una tupla de dos elementos (que son
    las coordenadas x e y de la vibora), inicialmente en el centro del tablero.
    '''
    vibora = []
    vibora.append((int(ALTO_TABLERO/2), int(ANCHO_TABLERO/2)))
    return vibora

def actualizar_direccion(input_usuario, direccion_actual):
    '''
    Dada una cadena de caracteres ingresada por el usuario, devuelve la 
    direccion en la que se mueve la vibora, tomando el primer caracter 
    de la cadena ingresada que coincida con uno de los caracteres 
    que se utilizan para mover a la vibora. Si la vibora se mueve en una dirección
    vertical solamente permite cambiar a una dirección horizontal y viceversa.
    '''
    if direccion_actual in TECLAS_DIRECCIONES[0:2]:
        teclas_posibles = TECLAS_DIRECCIONES[2] + TECLAS_DIRECCIONES[3]
    else:
        teclas_posibles = TECLAS_DIRECCIONES[0] + TECLAS_DIRECCIONES[1]
    for c in input_usuario:
        if c in teclas_posibles:
            return c
    return direccion_actual

def avanzar_cabeza(vibora, direccion):
    '''
    Dadas las coordenadas de la vibora, la dirección en la que se está moviendo 
    y la tupla que contiene las teclas para mover a la vibora, 
    alarga a la vibora en la dirección del movimiento (para lo cual modifica la lista vibora).
    '''
    movimientos_posibles = ((-1, 0), (1, 0), (0, -1), (0, 1))
    indice_direccion = TECLAS_DIRECCIONES.index(direccion)
    movimiento = movimientos_posibles[indice_direccion]
    vibora.append((vibora[-1][0] + movimiento[0], vibora[-1][1] + movimiento[1]))

def avanzar_cola(vibora):
    '''
    Le saca el ultimo elemento a la lista que representa a la vibora, 
    lo que tiene el efecto de un avance de la cola de la vibora.
    '''
    vibora.pop(0)    

def comio_fruta(vibora, fruta):
    '''
    Dadas las coordenadas de la vibora y de la fruta, devuelve True si la vibora 
    se comió a la fruta o False en caso contrario
    '''
    return vibora[-1] == tuple(fruta)

def reubicar_fruta(vibora, fruta):
    '''
    Dadas las coordenadas de la vibora, la lista fruta y las dimensiones 
    del tablero (especificadas como constantes globales),
    ubica la fruta en algún lugar del tablero no ocupado por la vibora,
    para lo cual modifica la lista fruta.
    '''
    while True:
        candidata_a_fruta = []
        candidata_a_fruta.append(randrange(ALTO_TABLERO))
        candidata_a_fruta.append(randrange(ANCHO_TABLERO))
        if tuple(candidata_a_fruta) not in vibora:
            fruta[0:2] = candidata_a_fruta
            break

def perdio(vibora):
    '''
    Devuelve True si el usuario perdio (ya sea porque se comio a si mismo o
    porque la vibora salio del tablero) y False en caso contrario.
    '''
    return se_mordio(vibora) or salio_del_tablero(vibora)

def se_mordio(vibora):
    '''Dadas las coordenadas de la vibora, devuelve True si se mordio a si misma o False si no'''
    return vibora[-1] in vibora[:-1]

def salio_del_tablero(vibora):
    '''
    Dadas las coordenadas de la vibora y las dimensiones del tablero (especificadas como
    constantes globales), devuelve True si la vibora salio del tablero o False en caso contrario.
    '''
    cabeza_vibora = vibora[-1]
    return -1 in cabeza_vibora or cabeza_vibora[0] == ALTO_TABLERO or cabeza_vibora[1] == ANCHO_TABLERO

def imprimir_tablero(vibora, fruta):
    '''
    Dadas las coordenadas de la vibora y de la fruta y las dimensiones
    del tablero (especificadas como constantes globales),
    imprime el tablero en la pantalla usando los simbolos
    especificados como constantes globales.
    '''
    
    for i in range(ALTO_TABLERO):

        if i == 0: # "techo" del tablero
            print('_' * (ANCHO_TABLERO + 2))

        for j in range(ANCHO_TABLERO):

            if j == 0:
                print('|', end = '') # lateral izquierdo
            
            if j == ANCHO_TABLERO - 1:
                fin_linea = '|\n' # lateral derecho
            else:
                fin_linea = ''

            if (i, j) in vibora:
                print(SIMBOLO_VIBORA, end = fin_linea)
            elif [i, j] == fruta:
                print(SIMBOLO_FRUTA, end = fin_linea)
            else:
                print(' ', end = fin_linea)

        if i == ALTO_TABLERO - 1:
            print('¯' * (ANCHO_TABLERO + 2)) # "piso" del tablero

def imprimir_comandos():
    '''Imprime las teclas que se usan para mover a la vibora (instrucciones).'''
    direcciones = ('arriba', 'abajo', 'izquierda', 'derecha')
    print('Comandos:')
    print()
    for i in range(len(TECLAS_DIRECCIONES)):
        print(str(direcciones[i]) + ': ' + str(TECLAS_DIRECCIONES[i]))
    print()

def imprimir_avance(longitud_vibora):
    '''
    Imprime el estado de avance en el juego 
    (cuantas frutas comió y cuántas faltan para ganar).
    '''
    frutas_faltan = LONGITUD_MAXIMA - longitud_vibora
    print('Frutas comidas: ' + str(longitud_vibora - 1))
    print('Frutas restantes para ganar: ' + str(frutas_faltan))

def imprimir_mensaje_final(longitud_vibora):
    '''Imprime el mensaje final al usuario'''
    print() # para dejar un espacio
    if longitud_vibora == LONGITUD_MAXIMA:
        print('Ganaste, felicitaciones!!!')
    else:
        print('Buena suerte en el próximo intento...')

main()
