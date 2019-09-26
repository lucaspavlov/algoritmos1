#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 23:17:41 2019

@author: Lucas
"""

from terminal import clear_terminal, timed_input
from random import randrange
from time import sleep
from modulosnake import actualizar_estado, reubicar_fruta, crear_tablero, actualizar_direccion, inicializar_tablero, imprimir_tablero, salir, imprimir_mensaje_final, pausa, salio_del_tablero

ANCHO_TABLERO = 20 # ancho del tablero, M
ALTO_TABLERO = 18 # alto del tablero, N
LONGITUD_MAXIMA = 10
DT = 0.2 # paso temporal (en segundos) entre iteraciones, si es mas chico la vibora va mas rapido
TABLERO_VACIO = crear_tablero(ANCHO_TABLERO, ALTO_TABLERO)
DIRECCIONES_POSIBLES = ('w', 's', 'a', 'd') # tupla con las cuatro direcciones posibles, w (arriba), s (abajo), a (izquierda), d (derecha)

fruta = []
fruta.append(randrange(ALTO_TABLERO))
fruta.append(randrange(ANCHO_TABLERO))

# coloco inicialmente la vibora en el centro
vibora = []
vibora.append([int(ALTO_TABLERO/2)])
vibora.append([int(ANCHO_TABLERO/2)])


direccion = DIRECCIONES_POSIBLES[randrange(4)] # inicialmente va en una direccion aleatoria
longitud = 1 # la vibora arranca teniendo longitud 1

#salir = False
p = False

while len(vibora[0]) < LONGITUD_MAXIMA:
    input_usuario = tuple(timed_input(DT))
    if not p:
        direccion = actualizar_direccion(input_usuario, direccion)
        
        comio_fruta, se_mordio = actualizar_estado(vibora, direccion, fruta)
                
        if comio_fruta:
            fruta = reubicar_fruta(vibora, ANCHO_TABLERO, ALTO_TABLERO)
        
        if se_mordio or salir(input_usuario) or salio_del_tablero(vibora, ANCHO_TABLERO, ALTO_TABLERO): # quit
            break
        
        tablero = inicializar_tablero(fruta, vibora, TABLERO_VACIO)
            
        clear_terminal()
        imprimir_tablero(tablero)
        
    p = pausa(input_usuario, p)

            
imprimir_mensaje_final(len(vibora[0]), LONGITUD_MAXIMA)
