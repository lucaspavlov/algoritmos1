#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:40:27 2019

@author: Lucas
"""

from terminal import clear_terminal, timed_input
from random import randrange
from time import sleep
from modulosnake import actualizar_estado, reubicar_fruta

ancho_tablero = 10 # ancho del tablero, M
alto_tablero = 18 # alto del tablero, N

fila = []
for i in range(ancho_tablero):
    fila.append(0) # creo una fila inicialmente con todos ceros (vacía)

tablero_vacio = []
for j in range(alto_tablero):
    tablero_vacio.append(tuple(fila)) # armo el tablero a partir de las filas
#tablero_vacio = ['' * ancho_tablero for i in range(alto_tablero)]

tablero_vacio = tuple(tablero_vacio)
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
t_espera_max = 2 # maximo tiempo de espera para que el usuario ingrese una direccion
salir = False

while len(vibora_fila) < longitud_maxima:
    #sleep(dt)
    input_usuario = tuple(timed_input(dt))
    #input_usuario = input('Ingresar direccion: ')
    for i in input_usuario:
        if i in direcciones_posibles:
            direccion = i
            break
        if i == 'q':
            salir = True
            break
    if salir: # quit
        break
    comio_fruta, se_mordio = actualizar_estado(vibora_fila, vibora_columna, direccion, fruta_fila, fruta_columna)
    
    if vibora_fila[len(vibora_fila)-1] < 0 or vibora_fila[len(vibora_fila)-1] >= alto_tablero or vibora_columna[len(vibora_fila)-1] < 0 or vibora_columna[len(vibora_fila)-1] >= ancho_tablero:
        print('Te fuiste del tablero')
        break
    
    if comio_fruta:
        fruta_fila, fruta_columna = reubicar_fruta(vibora_fila, vibora_columna, ancho_tablero, alto_tablero)
    
    tablero = [list(x) for x in tablero_vacio]
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if i == fruta_fila and j == fruta_columna:
                tablero[i][j] = 2
        for k in range(len(vibora_fila)):
            tablero[vibora_fila[k]][vibora_columna[k]] = 1
    
    clear_terminal()
    for i in range(len(tablero)):
        print(tablero[i])
    
    if se_mordio:
        print('Las viboras comen frutas, no viboras')
        break
    
if len(vibora_fila) == longitud_maxima:
    print('Felicitaciones !')
else:
    print('Seguí participando.')
