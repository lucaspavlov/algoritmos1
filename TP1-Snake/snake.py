#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 23:17:41 2019

@author: Lucas
"""

from terminal import clear_terminal, timed_input
from random import randrange
from time import sleep

ANCHO_TABLERO = 20 # ancho del tablero, M
ALTO_TABLERO = 18 # alto del tablero, N
LONGITUD_MAXIMA = 3
DT = 0.2 # paso temporal (en segundos) entre iteraciones, si es mas chico la vibora va mas rapido
DIRECCIONES_POSIBLES = ('w', 's', 'a', 'd') # tupla con las cuatro direcciones posibles, w (arriba), s (abajo), a (izquierda), d (derecha)

def main():
    
    tablero, fruta, vibora = inicializar(ANCHO_TABLERO, ALTO_TABLERO)
    
    direccion = DIRECCIONES_POSIBLES[randrange(4)] # inicialmente va en una direccion aleatoria
    
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
            
            modificar_tablero(fruta, vibora, tablero)
            
            clear_terminal()
            imprimir_tablero(tablero)
            
        p = pausa(input_usuario, p)
    
    imprimir_mensaje_final(len(vibora[0]), LONGITUD_MAXIMA)


def actualizar_estado(vibora, direccion, fruta):
    '''Dadas las coordenadas de la vibora y de la fruta y la dirección en la que se está moviendo la vibora, devuelve dos booleanos, uno que indica si la vibora comio una fruta en ese movimiento, y otro que indica si se mordio a si misma'''
    if direccion == 'w':
        vibora[0].append(vibora[0][len(vibora[0])-1] - 1)
        vibora[1].append(vibora[1][len(vibora[1])-1])
    if direccion == 's':
        vibora[0].append(vibora[0][len(vibora[0])-1] + 1)
        vibora[1].append(vibora[1][len(vibora[1])-1])
    if direccion == 'a':
        vibora[0].append(vibora[0][len(vibora[0])-1])
        vibora[1].append(vibora[1][len(vibora[1])-1] - 1)
    if direccion == 'd':
        vibora[0].append(vibora[0][len(vibora[0])-1])
        vibora[1].append(vibora[1][len(vibora[1])-1] + 1)
    if vibora[0][len(vibora[0])-1] != fruta[0] or vibora[1][len(vibora[1])-1] != fruta[1]:
        vibora[0].pop(0)
        vibora[1].pop(0)
        comio_fruta = False
    else:
        comio_fruta = True
    se_mordio = False
    for k in range(len(vibora[0])-1):
        if vibora[0][k] == vibora[0][len(vibora[0])-1] and vibora[1][k] == vibora[1][len(vibora[0])-1]:
            se_mordio = True
            break
    return comio_fruta, se_mordio

def reubicar_fruta(vibora, ancho_tablero, alto_tablero):
    '''Dadas las coordenadas de la vibora y las dimensiones del tablero, ubica la fruta en algún lugar del tablero no ocupado por la vibora'''
    while True:
        fruta = []
        fruta.append(randrange(alto_tablero))
        fruta.append(randrange(ancho_tablero))
        if fruta[0] in vibora[0] and fruta[1] in vibora[1]:
            pass
        else:
            return fruta
    
    #return vibora[0], vibora[1]

def actualizar_direccion(input_usuario, direccion_actual, tecla_abajo = 's', tecla_arriba = 'w', tecla_izquierda = 'a', tecla_derecha = 'd'):
    '''Dada una cadena de caracteres ingresada por el usuario, actualiza la direccion en la que se mueve la vibora'''
    if direccion_actual == tecla_abajo or direccion_actual == tecla_arriba:
        teclas_posibles = tecla_izquierda + tecla_derecha
    else:
        teclas_posibles = tecla_abajo + tecla_arriba
    for c in input_usuario:
        if c in teclas_posibles:
            return c
    return direccion_actual

def pausa(input_usuario, pausa_activada, tecla_pausa = 'p'):
    '''Función que recibe la cadena ingresada por el usuario y el estado actual del programa (en pausa o no como booleano, True o False). Si el usuario apretó la tecla de pausa, devuelve False si el juego estaba en pausa o True si no lo estaba'''
    for c in input_usuario:
        if c == tecla_pausa:
            return not pausa_activada
    return pausa_activada

def salir(input_usuario, tecla_salir = 'q'):
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

main()
