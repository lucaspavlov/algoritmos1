# Ejercicio 7.11 de la guia (Algoritmos I)
def texto_a_pagina(texto, longitud_maxima):
    '''
    Dado un texto, lo divide en una lista de renglones con un largo maximo
    (cortando en los espacios), y devuelve esa lista.
    '''
    renglones = []
    p = 0
    while len(texto) - p > longitud_maxima:
        renglon = texto[p:p+longitud_maxima]
        for i in range(len(renglon)):
            pos = len(renglon)-1-i
            caracter = renglon[pos]
            if caracter == ' ':
                renglones.append(renglon[0:pos+1])
                p += pos + 1
                break
            elif  i == len(renglon)-1: # en el caso de que no haya ningun espacio para poder cortar, mete todo el renglon
                renglones.append(renglon)
                p += len(renglon)
                break
    renglones.append(texto[p:]) # agrego lo que falta (una vez que sali del while queda un poco)
    return renglones
