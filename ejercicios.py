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
        
# Ejercicio 3.1
        
def a_segundos(h, m, s):
    S = 3600 * h + 60 * m + s
    return S

def a_hms(S):
    h = S // 3600
    m = (S - h * 3600) // 60
    s = S - h * 3600 - m * 60
    return h, m, s

# Ejercicio 3.2
    
h1 = int(input('Cantidad de horas del primer intervalo:'))
m1 = int(input('Cantidad de minutos del primer intervalo:'))
s1 = int(input('Cantidad de segundos del primer intervalo:'))

h2 = int(input('Cantidad de horas del segundo intervalo:'))
m2 = int(input('Cantidad de minutos del segundo intervalo:'))
s2 = int(input('Cantidad de segundos del segundo intervalo:'))

H, M, S = a_hms(a_segundos(h1, m1, s1) + a_segundos(h2, m2, s2))
print('La suma de los intervalos es igual a ' + str(H) + ' horas, ' + str(M) + ' minutos y ' + str(S) + ' segundos.')

# Ejercicio 3.3, se puede hacer mejor? sin hacer todos los productos a mano? por ej como lo generalizaria si en vez de 4 son n numeros con n grande

def mayor_producto(n1, n2, n3, n4):
    prod = n1 * n2
    prod = max(prod, n1 * n3)
    prod = max(prod, n1 * n4)
    prod = max(prod, n2 * n3)
    prod = max(prod, n2 * n4)
    prod = max(prod, n3 * n4)
    return prod

# Ejercicio 3.4
    
def norma(x, y, z):
    return (x ** 2 + y ** 2 + z ** 2) ** 0.5

def diferencia(x1, y1, z1, x2, y2, z2):
    dx = x1 - x2
    dy = y1 - y2
    dz = z1 - z2
    return dx, dy, dz

def producto_vec(x1, y1, z1, x2, y2, z2):
    pv1 = y1 * z2 - z1 * y2
    pv2 = z1 * x2 - x1 * z2
    pv3 = x1 * y2 - y1 * x2
    return pv1, pv2, pv3

def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    ABx, ABy, ABz = diferencia(x1, y1, z1, x2, y2, z2)
    BCx, BCy, BCz = diferencia(x2, y2, z2, x3, y3, z3)
    pv1, pv2, pv3 = producto_vec(ABx, ABy, ABz, BCx, BCy, BCz)
    area = norma(pv1, pv2, pv3) / 2
    return area

#def area_cuadrilatero(x1, y1, x2, y2, x3, y3, x4, y4): # no se como hacerlo... preguntar
    
# Ejercicio 4.1a
    
def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
def es_primo(n):
    if es_par(n):
        return False
    elif n == 1:
        return False
    else:
        N = int((n - 1) / 2) # voy a probar dividiendo a n por todos los impares hasta este numero, ya que mas alla de ese numero no tiene sentido porque es mas grande que la mitad de n
        for i in range(3, N + 1):
            if not es_par(i): # solamente me fijo en los impares (mayores a 1), porque en esta parte ya se que n es impar
                if n % i == 0:
                    return False # si para algun impar la division de n por i tiene resto cero, es decir n es divisible por i, entonces el numero no es primo ya que tiene un divisor impar mayor a 1. En ese caso devuelvo False ya que el numero no es primo, y salgo de la iteracion y de la funcion
        return True # si llegue hasta aca es porque n no tiene ningun divisor impar mayor a 1, es decir, n es primo
   
# Ejercicio 4.2
    
def abs_propia(x):
    if x >= 0:
        return x
    else:
        return -x
    
# Ejercicio 4.3, preguntar    
    
#def imprimir_matriz_identidad(n):
#    for i in range(n):
        
