#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 23:17:41 2019

@author: Lucas
"""

from terminal import clear_terminal, timed_input
from random import randrange
from time import sleep
from modulosnake import actualizar_estado, reubicar_fruta, crear_tablero, actualizar_direccion, inicializar_tablero, imprimir_tablero, salir

ancho_tablero = 20 # ancho del tablero, M
alto_tablero = 18 # alto del tablero, N

tablero_vacio = crear_tablero(ancho_tablero, alto_tablero)
#tablero = list(tablero_vacio)
#tablero = [list(x) for x in tablero_vacio]
# en el tablero, si no hay nada lo represento con un cero, si está la vibora lo represento con 1, si está la manzana con -1

fruta_fila = randrange(alto_tablero)
fruta_columna = randrange(ancho_tablero)

# coloco inicialmente la vibora en el centro
vibora_fila = [int(alto_tablero/2)]
vibora_columna = [int(ancho_tablero/2)]

direcciones_posibles = ('w', 's', 'a', 'd') # tupla con las cuatro direcciones posibles, w (arriba), s (abajo), a (izquierda), d (derecha)

direccion = direcciones_posibles[randrange(4)] # inicialmente va en una direccion aleatoria
longitud = 1 # la vibora arranca teniendo longitud 1
longitud_maxima = 10
dt = 0.2 # paso temporal (en segundos) entre iteraciones, si es mas chico la vibora va mas rapido
t_espera_max = 0.2 # maximo tiempo de espera para que el usuario ingrese una direccion
#salir = False
pausa = False

while len(vibora_fila) < longitud_maxima:
    if not pausa:
        input_usuario = tuple(timed_input(dt))
        direccion = actualizar_direccion(input_usuario, direccion)
        if salir(input_usuario): # quit
            break
        if 'p' in input_usuario:
            pausa = not pausa
        comio_fruta, se_mordio = actualizar_estado(vibora_fila, vibora_columna, direccion, fruta_fila, fruta_columna)
        
        if vibora_fila[len(vibora_fila)-1] < 0 or vibora_fila[len(vibora_fila)-1] >= alto_tablero or vibora_columna[len(vibora_fila)-1] < 0 or vibora_columna[len(vibora_fila)-1] >= ancho_tablero:
            print('Te fuiste del tablero')
            break
        
        if comio_fruta:
            fruta_fila, fruta_columna = reubicar_fruta(vibora_fila, vibora_columna, ancho_tablero, alto_tablero)
        
        tablero = inicializar_tablero(fruta_fila, fruta_columna, vibora_fila, vibora_columna, tablero_vacio)
            
        clear_terminal()
        imprimir_tablero(tablero)
        
        if se_mordio:
            print('Las viboras comen frutas, no viboras')
            break
    else:
        input_usuario = tuple(timed_input(dt))
        if 'p' in input_usuario:
            pausa = not pausa
            
if len(vibora_fila) == longitud_maxima:
    print('Felicitaciones !')
else:
    print('Seguí participando.')
