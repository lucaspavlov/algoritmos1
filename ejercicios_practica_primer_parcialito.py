# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:39:51 2019

@author: Porosos
"""

# segundo recuperatorio primer parcialito primer cuat 2013
def todas_las_rotaciones(cadena):
    '''Dada una cadena, devuelve todas las rotaciones posibles.'''
    lista_rotaciones = []
    for i in range(len(cadena)):
        cadena_rotada = cadena[i:len(cadena)] + cadena[0:i]
        lista_rotaciones.append(cadena_rotada)
    return lista_rotaciones

# Primer recuperatorio primer parcialito primer cuat 2014
def unique(l):
    '''Dada una lista, devuelve la misma sin elementos repetidos'''
    lista_sin_repeticiones = []
    for elemento in l:
        if elemento not in lista_sin_repeticiones:
            lista_sin_repeticiones.append(elemento)
    return lista_sin_repeticiones

def elementos_comunes_sin_repetir(lista1, lista2):
    '''Dadas dos listas, devuelve los elementos comunes a ambas, sin repeticiones'''
    lista1_sinrepetir = unique(lista1)
    repetidos = []
    for elemento in lista1_sinrepetir:
        if elemento in lista2:
            repetidos.append(elemento)
    return repetidos

# primer parcialito, segundo cuatrimestre de 2017

def maximos_columnas(matriz):
    '''Dada una matriz expresada como lista de listas, devuelve una lista con los maximos de cada columna'''
    max_cols = []
    for j in range(len(matriz[0])): # recorro columnas
        maximo = matriz[0][j]    
        for i in range(1,len(matriz)): # recorro filas
            maximo = max(maximo, matriz[i][j])
        max_cols.append(maximo)
    return max_cols
