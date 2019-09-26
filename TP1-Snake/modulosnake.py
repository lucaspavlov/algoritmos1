#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:03:21 2019
@author: Lucas
"""

from random import randrange

def actualizar_estado(vibora, direccion, fruta):
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
    '''Function que recibe la cadena ingresada por el usuario y el estado actual del programa (en pausa o no como booleano, True o False). Si el usuario apretó la tecla de pausa, devuelve False si el juego estaba en pausa o True si no lo estaba'''
    for c in input_usuario:
        if c == tecla_pausa:
            return not pausa_activada
    return pausa_activada

def salir(input_usuario, tecla_salir = 'q'):
    '''Funcion que recibe la entrada del usuario y devuelve True si el usuario apretó la tecla para salir del juego o False en caso contrario'''
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
    
    return tuple(tablero_vacio)

def inicializar_tablero(fruta, vibora, tablero_vacio):
    tablero = [list(x) for x in tablero_vacio]
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if i == fruta[0] and j == fruta[1]:
                tablero[i][j] = 2
        for k in range(len(vibora[0])):
            tablero[vibora[0][k]][vibora[1][k]] = 1
    return tablero
            
def imprimir_tablero(tablero):
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
    if longitud_vibora == longitud_maxima:
        print('Felicitaciones !')
    else:
        print('Seguí participando')
        
def salio_del_tablero(vibora, ancho_tablero, alto_tablero):
    if vibora[0][len(vibora[0])-1] < 0 or vibora[0][len(vibora[0])-1] >= alto_tablero or vibora[1][len(vibora[0])-1] < 0 or vibora[1][len(vibora[0])-1] >= ancho_tablero:
        return True
    return False

