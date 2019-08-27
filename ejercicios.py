#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 20:17:36 2019

@author: Lucas
"""

# Ejercicio 1.2

def perimetro_rectangulo(base,altura):
    perimetro = 2 * (base + altura)
    return perimetro

def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_rectangulo_puntos(x1,x2,y1,y2):
    base = abs(x2-x1)
    altura = abs(y2-y1)
    area = base * altura
    return area

def perimetro_circulo(radio):
    pi = 3.14159 # si no, lo puedo hacer con el modulo math o numpy (mas preciso)
    perimetro = 2 * pi * radio
    return perimetro

def area_circulo(radio):
    pi = 3.14159 # si no, lo puedo hacer con el modulo math o numpy (mas preciso)
    area = pi * radio ** 2
    return area

def volumen_esfera(radio):
    pi = 3.14159 # si no, lo puedo hacer con el modulo math o numpy (mas preciso)
    volumen = 4 * pi * radio ** 3 / 3
    return volumen

def hipotenusa(cateto1,cateto2):
    hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
    return hipotenusa

## Ejercicio 1.3

# Resultado de hacer
# for i in range(5):
#    print(i)

# 0
# 1
# 2
# 3
# 4
    
# Resultado de hacer
# for i in range(2,6):
#    print(i, i * 2)

# 2 4
# 3 6
# 4 8
# 5 10
    
# Ejercicio 1.4
    
def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial

# Ejercicio 1.5

def imprimir_operaciones(n1,n2):
    suma = n1 + n2
    resta = n1 - n2
    multiplicacion = n1 * n2
    division = n1 / n2
    print(str(n1) + ' + ' + str(n2) + ' = ' + str(suma))
    print(str(n1) + ' - ' + str(n2) + ' = ' + str(resta))
    print(str(n1) + ' * ' + str(n2) + ' = ' + str(multiplicacion))
    print(str(n1) + ' / ' + str(n2) + ' = ' + str(division))

def imprimir_tabla(n):
    for i in range(1,10):
        print(str(n) + ' * ' + str(i) + ' = ' + str(n * i))


# Ejercicio 1.6

def imprimir_n_veces(palabra, n):
    for i in range(n):
        print(palabra, end = ' ') # asume que palabra es un string. podria hacer str(palabra) para hacerlo mas general

#palabra = input('Escriba una palabra: ')
#imprimir_n_veces(palabra, 1000)
        
# Ejercicio 2.1
        
def capital_final(capital_inicial,tasa,anios):
    capital_final = capital_inicial * (1 + tasa / 100) ** anios
    return capital_final

capital_inicial = float(input('Capital inicial? '))
tasa = float(input('Tasa de interes? '))
anios = float(input('Cuántos años? '))
print('Capital final = ' + str(capital_final(capital_inicial, tasa, anios)))

# Ejercicio 2.2

def farenheit_a_celsius(F):
    C = 5 / 9 * (F -32)
    return C

# farenheit = 32
# celsius = farenheit_a_celsius(farenheit)
    
# Ejercicio 2.3
print('Farenheit', 'Celsius')
for i in range(13):
    F = 10 * i
    print(F, farenheit_a_celsius(F))
    
# Ejercicio 2.4
n1 = int(input('Ingrese un numero natural: ')) # asumo que es entero
n2 = int(input('Ingrese otro numero natural: ')) # asumo que es entero

for n in range(n1, n2 + 1):
    if n % 2 == 0:
        print(n)
        
# Ejercicio 2.5 - numeros triangulares
        
n = int(input('Ingrese un número natural: '))
N = 0
for i in range(1, n + 1):
    N = N + i
    print(i, N)

# usando la formula de Gauss. Esta tiene mas operaciones (la otra con una en cada iteracion funciona, obviamente usando el resultado de la anterior)
for i in range(1, n + 1):
    print(i, i*(i+1)/2)
    
# Ejercicio 2.6
# n = input('A cuántos números quiere tomarle el factorial?')
# como hacerlo? como acumulo los numeros? (quiero preguntar todos los numeros y luego imprimir todos los factoriales)
    
# Ejercicio 2.7 - domino
#c = 0
for i in range(7):
    for j in range(i + 1):
        print(i, j)
        c += 1 # al final debe dar 28, la cantidad de fichas del domino
        
# Ejercicio 2.8 , simplemente cambiar 7 por n + 1 con n la cantidad de numeros
for i in range(n + 1):
    for j in range(i + 1):
        print(i, j)
