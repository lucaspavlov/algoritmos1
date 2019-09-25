#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:03:21 2019
@author: Lucas
"""

from random import randrange

def actualizar_estado(vibora_fila, vibora_columna, direccion, fruta_fila, fruta_columna):
    if direccion == 'w':
        vibora_fila.append(vibora_fila[len(vibora_fila)-1] - 1)
        vibora_columna.append(vibora_columna[len(vibora_columna)-1])
    if direccion == 's':
        vibora_fila.append(vibora_fila[len(vibora_fila)-1] + 1)
        vibora_columna.append(vibora_columna[len(vibora_columna)-1])
    if direccion == 'a':
        vibora_fila.append(vibora_fila[len(vibora_fila)-1])
        vibora_columna.append(vibora_columna[len(vibora_columna)-1] - 1)
    if direccion == 'd':
        vibora_fila.append(vibora_fila[len(vibora_fila)-1])
        vibora_columna.append(vibora_columna[len(vibora_columna)-1] + 1)
    if vibora_fila[len(vibora_fila)-1] != fruta_fila or vibora_columna[len(vibora_columna)-1] != fruta_columna:
        vibora_fila.pop(0)
        vibora_columna.pop(0)
        comio_fruta = False
    else:
        comio_fruta = True
    se_mordio = False
    for k in range(len(vibora_fila)-1):
        if vibora_fila[k] == vibora_fila[len(vibora_fila)-1] and vibora_columna[k] == vibora_columna[len(vibora_fila)-1]:
            se_mordio = True
            break
    return comio_fruta, se_mordio

def reubicar_fruta(vibora_fila, vibora_columna, ancho_tablero, alto_tablero):
    while True:
        fruta_fila = randrange(alto_tablero)
        fruta_columna = randrange(ancho_tablero)
        if fruta_fila in vibora_fila and fruta_columna in vibora_columna:
            pass
        else:
            return fruta_fila, fruta_columna
    
    #return vibora_fila, vibora_columna

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

def inicializar_tablero(fruta_fila, fruta_columna, vibora_fila, vibora_columna, tablero_vacio):
    tablero = [list(x) for x in tablero_vacio]
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if i == fruta_fila and j == fruta_columna:
                tablero[i][j] = 2
        for k in range(len(vibora_fila)):
            tablero[vibora_fila[k]][vibora_columna[k]] = 1
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
