from terminal import clear_terminal, timed_input
from random import randrange, choice
from ejercicio_7_11 import texto_a_pagina

TECLAS_DIRECCIONES = ('w', 's', 'a', 'd') # tupla con las cuatro direcciones posibles en la forma (arriba, abajo, izquierda, derecha)
SIMBOLO_VIBORA = '#'
SIMBOLO_FRUTA = '*'
SIMBOLO_OBSTACULOS = chr(9632)
NIVELES = 3

def main():
    '''
    Flujo principal del juego snake.
    '''

    info_especiales = leer_especiales()
    imprimir_bienvenida()
    esperar_instruccion(' ')
    nivel_alcanzado = snake(info_especiales)
    imprimir_mensaje_final(nivel_alcanzado)

def snake(info_especiales):
    '''
    Ejecuta el juego de Snake, pasando por los distintos niveles hasta que el
    usuario gane (pase todos los niveles) o pierda. Devuelve el valor del ultimo
    nivel jugado por el usuario si el usuario perdio, o la cantidad de niveles
    totales + 1 si el usuario gano.
    '''
    nivel = 1
    while nivel <= NIVELES:
        paso_de_nivel = jugar_nivel(nivel, info_especiales)
        if paso_de_nivel:
            nivel += 1
            if nivel <= NIVELES: # se cumple siempre que el usuario no haya ganado el juego
                esperar_instruccion(' ')
        else:
            break

    return nivel

def jugar_nivel(nivel, info_especiales):
    '''
    Juego de un nivel de Snake++. Dadas las caracteristicas del nivel (longitud
    de la vibora necesaria para pasar de nivel, tiempo de reaccion inicial,
    dimensiones del tablero, posiciones de los obstaculos y especiales que
    pueden aparecer) y la descripcion de los especiales, ejecuta el juego del
    snake para un dado nivel. Devuelve True si el usuario paso de nivel o False
    en caso contrario.
    '''
    longitud_maxima, dt, dimensiones_tablero, obstaculos, especiales = leer_nivel(nivel)
    vibora, fruta, direccion, especial = estado_inicial(dimensiones_tablero, obstaculos, especiales)
    mochila = crear_mochila(info_especiales, especiales)

    while len(vibora) < longitud_maxima:

        input_usuario = timed_input(dt)

        direccion = actualizar_direccion(input_usuario, direccion)

        avanzar_cabeza(vibora, direccion)

        if comio_fruta(vibora, fruta):
            reubicar_fruta(vibora, obstaculos, especial, fruta, dimensiones_tablero)
        else:
            avanzar_cola(vibora)

        if comio_especial(vibora, especial):
            agregar_a_mochila(mochila, especial)
            reubicar_especial(vibora, obstaculos, fruta, especial, especiales, dimensiones_tablero)

        dt = efecto_especial(input_usuario, mochila, vibora, direccion, dt)

        if perdio(vibora, obstaculos, dimensiones_tablero):
            return False

        imprimir_juego(nivel, vibora, fruta, obstaculos, \
        especial, dimensiones_tablero, mochila, longitud_maxima)
    return True

def estado_inicial(dimensiones_tablero, obstaculos, especiales):
    '''
    Dadas las dimensiones del tablero y los caracteres utilizados para mover a
    la vibora (especificados como constante global), devuelve la posicion
    inicial de la vibora, la posición inicial de la fruta, la dirección
    inicial en la que se mueve la vibora (que es aleatoria) y la posición y el
    tipo de especial presente en el tablero inicialmente.
    '''

    vibora = crear_vibora(obstaculos, dimensiones_tablero)

    fruta = list(vibora[0])
    especial = [nuevo_especial(especiales)]
    especial.append(list(vibora[0]))

    reubicar_fruta(vibora, obstaculos, especial, fruta, dimensiones_tablero) # a posicion aleatoria

    reubicar_especial(vibora, obstaculos, fruta, especial, especiales, dimensiones_tablero)

    direccion = TECLAS_DIRECCIONES[randrange(4)]

    return vibora, fruta, direccion, especial

def crear_vibora(obstaculos, dimensiones_tablero):
    '''
    Devuelve una lista con una tupla de dos elementos (que son
    las coordenadas x e y de la vibora), inicialmente en el centro del tablero
    (salvo que justo haya un obstáculo ahí, en cuyo caso la vibora empieza en
    una posición aleatoria).
    '''
    vibora = []
    alto_tablero, ancho_tablero = dimensiones_tablero
    posicion_inicial = ((int(alto_tablero/2), int(ancho_tablero/2)))
    vibora.append(posicion_inicial)
    while posicion_inicial in obstaculos:
        posicion_inicial = (randrange(alto_tablero), randrange(ancho_tablero))
        vibora[0] = posicion_inicial
    return vibora

def crear_mochila(info_especiales, especiales_nivel):
    '''
    Devuelve un diccionario cuyas claves son una tupla con el simbolo, aspecto,
    alteracion, tecla y descripcion del especial, y los valores, que representan
    la cantidad de especiales en la mochila, son cero. La mochila contiene
    solamente los especiales que pueden aparecer en el presente nivel.
    En las claves, aspecto, tecla y descripcion son cadenas y alteracion es
    entero o flotante dependiendo de si aspecto es 'LARGO' o 'VELOCIDAD' respectivamente.
    '''
    mochila = {}

    for simbolo, aspecto, alteracion_cadena, tecla, descripcion in info_especiales:
        if simbolo in especiales_nivel: # deberia suceder siempre si los archivos estan bien
            if aspecto == 'LARGO':
                alteracion = int(alteracion_cadena)
            elif aspecto == 'VELOCIDAD':
                alteracion = float(alteracion_cadena)
            mochila[(simbolo, tecla, aspecto, alteracion, descripcion)] = 0

    return mochila

def leer_especiales():
    '''
    Lee el archivo especiales.csv y devuelve la información (simbolo y efecto)
    de los distintos tipos de especiales posibles en forma de lista.
    '''
    info_especiales = []
    with open('especiales.csv') as archivo_especiales:
        linea = archivo_especiales.readline().rstrip().split(',')
        while linea[0] != '':
             info_especiales.append(linea)
             linea = archivo_especiales.readline().rstrip().split(',')
    return info_especiales

def leer_nivel(nivel):
    '''
    Dado un número de nivel, lee la información relativa al mismo (longitud máxima
    para pasar de nivel, tiempo de reacción inicial, dimensiones del tablero,
    coordenadas de los obstáculos y especiales válidos) contenida en un archivo
    .txt), la procesa y la devuelve en forma de tupla.
    '''
    lineas_nivel = []
    with open('nivel_' + str(nivel) + '.txt', 'r') as nivel:
        linea = nivel.readline().rstrip()
        while linea != '':
           lineas_nivel.append(linea)
           linea = nivel.readline().rstrip()

    longitud_maxima = int(lineas_nivel[0])
    dt = float(lineas_nivel[1])
    alto_tablero, ancho_tablero = [int(dim) for dim in lineas_nivel[2].split('x')]
    coordenadas_obstaculos = cadena_a_coordenadas(lineas_nivel[3])
    simbolos_especiales = tuple(lineas_nivel[4].split(','))

    return (longitud_maxima, dt, (alto_tablero, ancho_tablero), \
    coordenadas_obstaculos, simbolos_especiales)

def cadena_a_coordenadas(cadena):
    '''
    Dada una cadena que contiene coordenadas de numeros enteros en la forma
    x1,y1;x2,y2;..., las devuelve una tupla de tuplas ((x1, y1), (x2, y2), ...),
    en donde x1, y1, ..., son enteros.
    '''
    lista_cadenas = [l.split(',') for l in cadena.split(';')]
    obstaculos = []
    for coordenadas in lista_cadenas:
        obstaculos.append(tuple([int(l) for l in coordenadas]))
    return tuple(obstaculos)

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
    se comió a la fruta o a un especial o False en caso contrario
    '''
    return vibora[-1] == tuple(fruta)

def comio_especial(vibora, especial):
    '''Devuelve True si la vibora comio un especial o False en caso contrario'''
    return vibora[-1] == tuple(especial[1])

def reubicar(vibora, obstaculos, fijo, a_reubicar, dimensiones_tablero):
    '''
    Dadas las coordenadas de la vibora, los obstaculos, las dimensiones del
    tablero, un elemento que queda fijo (puede ser la fruta o un especial) y
    otro que hay que reubicar (es el especial o la fruta, el que no queda fijo),
    reubica al elemento a reubicar en una posicion aleatoria que no coincida con
    la vibora, los obstaculos ni el elemento fijo que esta en el tablero.
    '''
    alto_tablero, ancho_tablero = dimensiones_tablero
    while True:
        candidato = []
        candidato.append(randrange(alto_tablero))
        candidato.append(randrange(ancho_tablero))
        if tuple(candidato) not in vibora and tuple(candidato) not in obstaculos and candidato != fijo:
            a_reubicar[0:2] = candidato
            break

def reubicar_fruta(vibora, obstaculos, especial, fruta, dimensiones_tablero):
    '''Reubica la fruta (modificando la lista fruta) en una posicion disponible del tablero.'''
    reubicar(vibora, obstaculos, especial[1], fruta, dimensiones_tablero)

def reubicar_especial(vibora, obstaculos, fruta, especial, especiales, dimensiones_tablero):
    '''
    Reubica el especial (modificando la segunda entrada de la lista especial)
    en una posicion disponible del tablero. Ademas modifica la primera entrada
    de la lista especial con el simbolo del nuevo especial presente en el tablero.
    '''
    reubicar(vibora, obstaculos, fruta, especial[1], dimensiones_tablero)
    especial[0] = choice(especiales)

def agregar_a_mochila(mochila, especial):
    '''
    Agrega un especial a la mochila.
    '''
    for clave in mochila.keys():
        if especial[0] == clave[0]:
            mochila[clave] += 1
            break

def sacar_de_mochila(mochila, especial):
    '''
    Saca un especial de la mochila. Si la mochila no tiene ningun elemento
    del especial, no hace nada.
    '''
    for clave in mochila.keys():
        if especial[0] == clave[0]:
            mochila[clave] = max(mochila[clave] - 1, 0)
            break

def nuevo_especial(especiales):
    '''
    Dado una tupla con especiales posibles, devuelve uno al azar.
    '''
    return choice(especiales)

def activo_especial(input_usuario, mochila, longitud_vibora):
    '''
    Devuelve una tupla (aspecto, alteracion) si el usuario activó un especial
    valido (y en ese caso lo saca de la mochila) o devuelve una tupla con
    ('No se activo', 0) en caso contrario. Un especial que disminuya la longitud
    se considera inválido si hace que la longitud de la vibora sea menor a uno
    (en ese caso no se utiliza el especial y no se lo saca de la mochila).
    '''
    for c in input_usuario:
        for (simbolo, tecla, aspecto, alteracion, descripcion), valor in mochila.items():
            if c == tecla and valor > 0:
                if not (aspecto == 'LARGO' and longitud_vibora + alteracion < 1):
                    sacar_de_mochila(mochila, simbolo)
                    return (aspecto, alteracion)
    return ('No se activo', 0)

def especial_largo(vibora, alteracion, direccion):
    '''
    Alarga o acorta la vibora de acuerdo a la alteracion del especial utilizado.
    '''
    if alteracion > 0:
        for i in range(alteracion):
            avanzar_cabeza(vibora, direccion)
    else:
        for i in range(min(-alteracion, len(vibora)-1)): # asegura que la vibora tenga longitud al menos 1
            avanzar_cola(vibora)

def especial_velocidad(dt, alteracion):
    '''
    Aumenta o disminuye la velocidad de acuerdo a la alteracion del especial utilizado.
    '''
    return dt * alteracion

def efecto_especial(input_usuario, mochila, vibora, direccion, dt):
    '''
    Devuelve el nuevo valor de dt, que sera el mismo que el anterior si no se
    uso ningun especial o si se uso uno que modifique la longitud de la vibora,
    o diferente si se uso un especial que modifique el tiempo de reaccion.
    En caso de usar un especial que modifique la longitud de la vibora, modifica
    la lista vibora acordemente.
    '''
    (aspecto, alteracion) = activo_especial(input_usuario, mochila, len(vibora))

    if aspecto == 'LARGO':
        especial_largo(vibora, alteracion, direccion)
    elif aspecto == 'VELOCIDAD':
        dt = especial_velocidad(dt, alteracion)
    return dt

def perdio(vibora, obstaculos, dimensiones_tablero):
    '''
    Devuelve True si el usuario perdio (ya sea porque se comio a si mismo o
    porque la vibora salio del tablero) y False en caso contrario.
    '''
    return se_mordio(vibora) or salio_del_tablero(vibora, dimensiones_tablero) \
    or toco_obstaculo(vibora, obstaculos)

def toco_obstaculo(vibora, obstaculos):
    '''
    Devuelve True si la vibora toco un obstaculo o False en caso contrario
    '''
    return vibora[-1] in obstaculos

def se_mordio(vibora):
    '''Dadas las coordenadas de la vibora, devuelve True si se mordio a si misma o False si no'''
    return vibora[-1] in vibora[:-1]

def salio_del_tablero(vibora, dimensiones_tablero):
    '''
    Dadas las coordenadas de la vibora y las dimensiones del tablero (especificadas como
    constantes globales), devuelve True si la vibora salio del tablero o False en caso contrario.
    '''
    alto_tablero, ancho_tablero = dimensiones_tablero
    cabeza_vibora = vibora[-1]
    return -1 in cabeza_vibora or cabeza_vibora[0] == alto_tablero \
    or cabeza_vibora[1] == ancho_tablero

def esperar_instruccion(caracter):
    '''
    Bucle while del cual se sale solamente si el usuario apreta el caracter
    pasado por parámetro (que debe ser una cadena de longitud 1).
    '''
    while caracter not in timed_input(0.05):
        continue

def imprimir_nivel(nivel):
    '''
    Imprime el nivel actual y la cantidad total de niveles.
    '''
    print('Nivel ' + str(nivel) + ' de ' + str(NIVELES))

def imprimir_tablero(vibora, fruta, obstaculos, especial, dimensiones_tablero):
    '''
    Dadas las coordenadas de la vibora, la fruta, los obstáculos, los especiales
    y las dimensiones del tablero, imprime el tablero en la pantalla usando los
    simbolos especificados como constantes globales (salvo en los especiales que
    los simbolos vienen en la lista especiales).
    '''

    alto_tablero, ancho_tablero = dimensiones_tablero
    simbolo_especial, coordenadas_especial = especial

    for i in range(alto_tablero):

        if i == 0: # "techo" del tablero
            print('_' * (ancho_tablero + 2))

        for j in range(ancho_tablero):

            if j == 0:
                print('|', end = '') # lateral izquierdo

            if j == ancho_tablero - 1:
                fin_linea = '|\n' # lateral derecho
            else:
                fin_linea = ''

            if (i, j) in obstaculos:
                print(SIMBOLO_OBSTACULOS, end = fin_linea)
            elif (i, j) in vibora:
                print(SIMBOLO_VIBORA, end = fin_linea)
            elif [i, j] == fruta:
                print(SIMBOLO_FRUTA, end = fin_linea)
            elif [i, j] == coordenadas_especial:
                print(simbolo_especial, end = fin_linea)
            else:
                print(' ', end = fin_linea)

        if i == alto_tablero - 1:
            print('¯' * (ancho_tablero + 2)) # "piso" del tablero

def imprimir_simbolos():
    '''Imprime los simbolos de la fruta y de los obstaculos.'''
    print('Fruta : ' + SIMBOLO_FRUTA + ' | Obstaculos : ' + SIMBOLO_OBSTACULOS)

def imprimir_comandos():
    '''Imprime las teclas que se usan para mover a la vibora (instrucciones).'''
    direcciones = ('arriba', 'abajo', 'izquierda', 'derecha')
    print('Comandos:')
    print()
    for i in range(len(TECLAS_DIRECCIONES)):
        print(str(direcciones[i]) + ': ' + str(TECLAS_DIRECCIONES[i]))
    print()

def imprimir_avance(longitud_vibora, longitud_maxima, nivel):
    '''
    Imprime el estado de avance en el juego (cuantas frutas comió y cuántas
    faltan para ganar). Si el usuario pasó al siguiente nivel, imprime
    una instrucción.
    '''

    print('Longitud de la vibora: ' + str(longitud_vibora))
    print('Longitud necesaria para completar el nivel: ' + str(longitud_maxima))

    if longitud_vibora >= longitud_maxima and nivel < NIVELES:
        print('NIVEL COMPLETADO. Apretá la barra espaciadora para empezar el próximo nivel.')

def imprimir_mochila(mochila):
    '''
    Imprime los símbolos de los especiales disponibles del nivel, la cantidad
    de cada uno que hay en la mochila, la tecla que hay que usar para activarlos,
    y una descripción de su efecto.
    '''
    print('MOCHILA:')
    print('SIMBOLO || CANTIDAD || TECLA || DESCRIPCION')
    for clave, valor in mochila.items():
        simbolo, tecla, aspecto, alteracion, descripcion = clave
        print('   ' + simbolo, end = '')
        print('    ||    ' + str(valor), end = '')
        print('     ||   ' + tecla, end = '')
        print('   || ' + descripcion)
    print('')

def imprimir_juego(nivel, vibora, fruta, obstaculos, especial, dimensiones_tablero, mochila, longitud_maxima):
    '''Imprime el juego en la pantalla'''
    clear_terminal()
    imprimir_nivel(nivel)
    imprimir_tablero(vibora, fruta, obstaculos, especial, dimensiones_tablero)
    imprimir_simbolos()
    imprimir_mochila(mochila)
    imprimir_comandos()
    imprimir_avance(len(vibora), longitud_maxima, nivel)

def imprimir_instrucciones():
    '''Imprime las instrucciones del juego'''

    instrucciones = 'La viborita, representada con el simbolo '\
    + str(SIMBOLO_VIBORA) + ' empieza con longitud 1, y el objetivo para '\
    +'pasar de nivel es llegar a una longitud determinada, que se informa en cada '\
    +'nivel. La viborita se mueve hacia (arriba, abajo, izquierda, derecha) '\
    +'con las teclas ' + str(TECLAS_DIRECCIONES) + ' respectivamente. '\
    +'Para que la viborita crezca debe comer frutas, representadas con el simbolo '\
    + str(SIMBOLO_FRUTA) + '. Tambien tiene la posibilidad de crecer mediante '\
    +'el uso de especiales, que son poderes que se adquieren luego de comerlos en '\
    +'el tablero. En cada nivel hay especiales distintos, con distintos poderes que '\
    +'permiten alargar o acortar la vibora o aumentar o reducir su velocidad. '\
    +'Los simbolos y las teclas para activar los especiales se muestran en '\
    +'cada nivel en la mochila, en donde se puede ver la cantidad de especiales '\
    +'disponibles y el efecto de cada uno. El nivel termina cuando se llega a la '\
    +'longitud requerida, en cuyo caso se pasa de nivel, o cuando la vibora se come '\
    +'a si misma, sale del tablero, o toca un obstáculo, representados con el símbolo '\
    + SIMBOLO_OBSTACULOS + ', en cuyo caso pierde el juego. Al pasar de nivel '\
    +'se pierden los especiales que se tenían. La cantidad total de niveles '\
    +'es ' + str(NIVELES) + '.'

    print('Instrucciones para jugar:')
    for renglon in texto_a_pagina(instrucciones, 60):
        print(renglon)

def imprimir_bienvenida():
    '''Imprime el mensaje de bienvenida al usuario.'''
    clear_terminal()
    print('Bienvenido a Snake++, la versión recargada del clásico juego de la viborita.')
    print('Apretá la BARRA ESPACIADORA para empezar a jugar.')
    print('')
    imprimir_instrucciones()

def imprimir_mensaje_final(nivel_alcanzado):
    '''Imprime el mensaje final al usuario.'''
    print() # para dejar un espacio
    if nivel_alcanzado > NIVELES:
        print('Ganaste, felicitaciones!!!')
    else:
        print('Buena suerte en el próximo intento...')

main()
