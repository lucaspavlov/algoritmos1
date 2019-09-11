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
    
# Ejercicio 4.3   
    
def imprimir_matriz_identidad(n):
    ''' Funcion que, dado un entero n especificado como input, imprime la matriz identidad de dimensión n'''
    for i in range(1, n+1):
        line = ''
        for j in range(1, n+1):
            if i == j:
                line = line + '1 '
            else:
                line = line + '0 '
        print(line[:-1]) # el :-1 es solo para que no imprima el ultimo espacio, si uso solo print(line) igual imprime la matriz identidad pero con un espacio despues del ultimo digito
                
        
    
# Ejercicio 4.4a
def maxomin_polgrado2(a,b,c):
    ''' Encuentra el máximo o mínimo de un polinomio de grado 2, a*x^2+b*x+c, e indica si es máximo o mínimo'''
    if a > 0:
       maxomin = 'es mínimo'
    elif a < 0:
        maxomin = 'es máximo'
    else:
        print('El primer coeficiente no puede ser cero.')
        return
    
    maxomin_valor = - b / 2 / a
    return maxomin_valor, maxomin

# Ejercicio 4.4b
def raices(a,b,c):
    ''' Devuelve las raices, reales o complejas, de un polinomio de grado 2, a*x^2+b*x+c'''
    if a == 0:
        print('El primer coeficiente no puede ser cero')
        return
    if b ** 2 - 4 * a * c < 0:
        raiz1 = (- b + (4 * a * c - b ** 2)**0.5 * complex(0,1)) / 2 / a
        raiz2 = (- b - (4 * a * c - b ** 2)**0.5 * complex(0,1)) / 2 / a
    else:
        raiz1 = (- b + (b ** 2 - 4 * a * c) ** 0.5) / 2 / a
        raiz2 = (- b - (b ** 2 - 4 * a * c) ** 0.5) / 2 / a
    return raiz1, raiz2

# Ejercicio 4.4c
def interseccion_rectas(m1,b1,m2,b2):
    ''' Devuelve la intersección de dos rectas, dadas por y = m1*x+b1 y por y = m2*x+b2, como coordenadas (x,y)'''
    if m1 == m2:
        print('Las rectas tienen la misma pendiente')
        return
    x_interseccion = (b2 - b1) / (m1 - m2)
    y_interseccion = m1 * x_interseccion + b1
    return x_interseccion, y_interseccion

# Ejercicio 4.5a
def es_bisiesto(anio):
    '''Funcion que devuelve True si un año es bisiesto o False si no lo es'''
    if anio % 4 == 0:
        if anio % 400 == 0:
            return True
        if anio % 100 == 0:
            return False
        return True
    return False

# Ejercicio 4.5b
def cantidad_dias(mes,anio):
    '''Dado un mes y un año, devuelve la cantidad de dias que tiene ese mes'''
    if mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31
    else:
        return 30

def es_valida(dia, mes, anio):
    '''Dada una fecha, devuelve True si es válida o False si no lo es'''
    if dia % 1 != 0 or mes % 1 != 0 or anio % 1 != 0:
        return False # dias, meses o años no pueden no ser enteros
    if dia <= 0 or dia > 31 or mes <=0 or mes > 12:
        return False # dias y meses deben ser positivos y estar entre 1 y 31 o entre 1 y 12 respectivamente
    if mes == 2:
        if dia > 29:
            return False
        if es_bisiesto(anio):
            return True
        elif dia != 29:
            return True
    else:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            return True
        elif dia != 31:
            return True
    return False

def dias_hasta_fin_de_mes(dia, mes, anio):
    '''Dado un día, mes y año, devuelve la cantidad de días que faltan hasta fin de mes'''
    if not es_valida(dia, mes, anio):
        print('Fecha no válida')
        return
    return cantidad_dias(mes, anio) - dia

def dias_hasta_fin_de_anio(dia, mes, anio):
    '''Dado un día, mes y año, devuelve la cantidad de días que faltan hasta fin de año'''
    if not es_valida(dia, mes, anio):
        print('Fecha no válida')
        return
    dias_hasta_fin_de_anio = dias_hasta_fin_de_mes(dia, mes, anio)
    for m in range(mes + 1, 13):
        dias_hasta_fin_de_anio += cantidad_dias(m, anio)
    return dias_hasta_fin_de_anio

def dias_transcurridos_en_el_anio(dia, mes, anio):
    '''Dado un dia, mes y año, devuelve la cantidad de dias que pasaron en ese año'''
    if not es_valida(dia, mes, anio):
        print('Fecha no válida')
        return
    if es_bisiesto(anio):
        return 366 - dias_hasta_fin_de_anio(dia, mes, anio)
    else:
        return 365 - dias_hasta_fin_de_anio(dia, mes, anio)

def anios_meses_y_dias_transcurridos(dia1, mes1, anio1, dia2, mes2, anio2): # asume que dia1, mes1, anio1 es anterior a dia2, mes2, anio2
    '''Dados dos días, expresados como (día, mes, año), devuelve la cantidad de días, meses y años entre ambos'''
    if not es_valida(dia1, mes1, anio1) or not es_valida(dia2, mes2, anio2):
        print('Fecha no válida')
        return
    dias_hasta_fin_de_anio1 = dias_hasta_fin_de_anio(dia1, mes1, anio1)
    dias_transcurridos_en_el_anio2 = dias_transcurridos_en_el_anio(dia2, mes2, anio2)
    dias_totales = dias_hasta_fin_de_anio1 + dias_transcurridos_en_el_anio2
    for anio in range(anio1 + 1, anio2):
        if es_bisiesto(anio):
            dias_totales = dias_totales + 366
        else:
            dias_totales = dias_totales + 365
    anios = dias_totales // 365
    meses = (dias_totales - anios * 365) // 30
    dias = dias_totales - anios * 365 - meses * 30
    return anios, meses, dias

# Ejercicio 4.6
def nombre_del_dia(dia_del_anio):
    '''Dado un número de día de un año (entre 1 y 366), devuelve de qué día se trata asumiendo que el 1 de enero fue lunes'''
    if dia_del_anio % 1 != 0 or dia_del_anio < 1 or dia_del_anio > 366:
        print('Dia incorrecto, debe ser un entero entre 1 y 366')
        return
    d = dia_del_anio % 7
    if d == 1:
        return 'lunes'
    if d == 2:
        return 'martes'
    if d == 3:
        return 'miércoles'
    if d == 4:
        return 'jueves'
    if d == 5:
        return 'viernes'
    if d == 6:
        return 'sábado'
    if d == 0:
        return 'domingo'

# Ejercicio 4.8
def signo_zodiacal(dia, mes):
    if not es_valida(dia, mes, 2000):
        print('Fecha no valida')
        return
    if mes == 1:
        if dia < 21:
            signo = 'capricornio'
        else:
            signo = 'acuario'
    if mes == 2:
        if dia < 20:
            signo = 'acuario'
        else:
            signo = 'piscis'
    if mes == 3:
        if dia < 21:
            signo = 'piscis'
        else:
            signo = 'aries'
    if mes == 4:
        if dia < 21:
            signo = 'aries'
        else:
            signo = 'tauro'
    if mes == 5:
        if dia < 21:
            signo = 'tauro'
        else:
            signo = 'geminis'
    if mes == 6:
        if dia < 22:
            signo = 'geminis'
        else:
            signo = 'cancer'
    if mes == 7:
        if dia < 24:
            signo = 'cancer'
        else:
            signo = 'leo'
    if mes == 8:
        if dia < 24:
            signo = 'leo'
        else:
            signo = 'virgo'
    if mes == 9:
        if dia < 24:
            signo = 'virgo'
        else:
            signo = 'libra'
    if mes == 10:
        if dia < 23:
            signo = 'libra'
        else:
            signo = 'escorpio'
    if mes == 11:
        if dia < 22:
            signo = 'escorpio'
        else:
            signo = 'sagitario'
    if mes == 12:
        if dia < 22:
            signo = 'sagitario'
        else:
            signo = 'capricornio'
    return signo

ddmm = input('Ingrese el día y mes de su cumpleaños [en formato dd/mm]: ')
dia = int(ddmm[0:2])
mes = int(ddmm[3:5])
sgn = signo_zodiacal(dia, mes)
print(sgn)
            

# Ejercicio 5.1
quiere_seguir_ingresando = 'Si'
suma_notas = 0
cantidad_notas = 0
while quiere_seguir_ingresando == 'Si':
    suma_notas += float(input('Ingrese una nota: '))
    cantidad_notas += 1
    quiere_seguir_ingresando = input('Quiere seguir ingresando notas? [Si/No] ')
print('El promedio es ' + str(suma_notas / cantidad_notas))


# Ejercicio 5.2
def descomposicion_en_primos(n):
    '''Funcion que recibe por argumento un entero n e imprime su descomposicion en numeros primos (no devuelve nada)'''
    factor = n
    divisor = 2
    while factor != 1:
        if factor % divisor == 0:
            print(divisor)
            factor = factor / divisor
        else:
            divisor += 1

# Ejercicio 5.3a
            
CONTRASENIA = 'pincha'
intento = ''

while intento != CONTRASENIA:
    intento = input('Ingrese la contrasenia: ')
    if intento != CONTRASENIA:
        print('Contrasenia incorrecta, intente nuevamente')
        
# Ejercicio 5.3b
        
CONTRASENIA = 'pincha'
intento = ''
num_max_intentos = 5
num_intentos = 0

while intento != CONTRASENIA and num_intentos < num_max_intentos:
    intento = input('Ingrese la contrasenia: ')
    if intento != CONTRASENIA:
        print('Contrasenia incorrecta, intente nuevamente')
        num_intentos += 1
        if num_intentos == num_max_intentos:
            print('Número máximo de intentos alcanzados')

# Ejercicio 5.3c
        
import time
CONTRASENIA = 'pincha'
intento = ''
num_max_intentos = 5
num_intentos = 0

while intento != CONTRASENIA and num_intentos < num_max_intentos:
    intento = input('Ingrese la contrasenia: ')
    if intento != CONTRASENIA:
        print('Contrasenia incorrecta, intente nuevamente')
        num_intentos += 1
        if num_intentos == num_max_intentos:
            print('Número máximo de intentos alcanzados')
        time.sleep(num_intentos)


# Ejercicio 5.3d # preguntar si se espera que en el programa aparezca el ciclo while (dado que debe devolver True o False imagino que no)
def contrasenia_correcta():
    CONTRASENIA = 'pincha'
    intento = input('Ingrese la contrasenia: ')
    if intento != CONTRASENIA:
        return False
    else:
        return True

# Ejercicio 5.4
import random
N = 100 # numero maximo a generar
num = random.randrange(1, N + 1)
numero_ingresado = -1
while numero_ingresado != num:
    numero_ingresado = int(input('Ingrese un número: '))
    if numero_ingresado == num:
        print('Bingo!')
    elif numero_ingresado < num:
        print('El número ingresado es menor al número secreto')
    else:
        print('El número ingresado es mayor al número secreto')

# Ejercicio 5.5
def mcd_euclides(num1, num2):
    num_max = max(num1, num2)
    num_min = min(num1, num2)
    resto = 1
    while resto != 0:
        resto = num_max % num_min
        num_max = num_min
        num_min = resto
    return num_max

# Ejercicio 5.6
def es_potencia_de_dos(n):
    if n < 2:
        return False
    elif int(n**0.5) == n**0.5 or n == 2:
        return True
    else:
        return False

def suma_de_potencias_de_dos(num1, num2):
    num_min = min(num1, num2)
    num_max = max(num1, num2)
    sum_pot2 = 0
    for i in range(num_min, num_max+1):
        if es_potencia_de_dos(i):
            sum_pot2 = sum_pot2 + i
    return sum_pot2

# Ejercicio 5.7a - en realidad NO es esto lo que se pide, me equivoque
def divisores(n):
    lista_divisores = [] # se puede hacer sin listas?
    for i in range(1, n):
        if n % i == 0:
            lista_divisores.append(i)
    return lista_divisores

# Ejercicio 5.7a
def suma_divisores(n):
    '''Dado un número n, devuelve la suma de todos los divisores, excepto el mismo'''
    sum_div = 0
    for i in range(1, n):
        if n % i == 0:
            sum_div += i
    return sum_div

# Ejercicio 5.7b
def primeros_numeros_perfectos(m):
    '''Imprime los primeros m numeros perfectos, definidos como los números cuya suma de divisores es igual a el numero mismo'''
    np = 0
    i = 1
    while np < m:
        if suma_divisores(i) == i:
            print(i)
            np += 1
        i += 1

# Ejercicio 5.7c
def primeros_numeros_amigos(m):
    '''Imprime los primeros m numeros amigos'''
    np = 0
    i = 1
    j = 1
    while np < m:
        for j in range(1, i):
            if suma_divisores(i) == j and suma_divisores(j) == i:
                print(i, j)
                np += 1
        i += 1
        
# Ejercicio 5.7d, preguntar...
def primeros_numeros_amigos_masrapida(m):
    '''Imprime los primeros m numeros amigos'''
    np = 0
    i = 1
    j = 1
    while np < m:
        for j in range(1, i):
            j2 = i - j
            if suma_divisores(i) == j2 and suma_divisores(j2) == i:
                print(i, j2)
                np += 1
        i += 1

# Ejercicio 5.8
n = 0
suma = 0
cantidad_de_numeros_ingresados = 0
while n != -1:
    n = int(input('Ingrese un número natural (-1 para terminar): '))
    if n > 0:
        suma += n
        cantidad_de_numeros_ingresados += 1
    elif n != -1:
        print('El número debe ser natural.')
print('Se ingresaron ' + str(cantidad_de_numeros_ingresados) + ' numeros, cuya suma da ' + str(suma) + ' y, por lo tanto, el promedio de los mismos es ' + str(suma / cantidad_de_numeros_ingresados))

# Ejercicio 5.9a
def multiplos_menores_que_numero_confor(n1, n2):
    '''Dados dos numeros n1 y n2, devuelve la cantidad de multiplos de n1 que son menores que n2'''
    cantidad_de_multiplos_menores = 0
    for i in range(n1, n2):
        if i % n1 == 0:
            cantidad_de_multiplos_menores += 1
    return cantidad_de_multiplos_menores

# Ejercicio 5.9b
def multiplos_menores_que_numero_conwhile(n1, n2):
    '''Dados dos numeros n1 y n2, devuelve la cantidad de multiplos de n1 que son menores que n2'''
    cantidad_de_multiplos_menores = 0
    n = n1
    while n < n2:
        cantidad_de_multiplos_menores += 1
        n = (cantidad_de_multiplos_menores + 1) * n1
        
    return cantidad_de_multiplos_menores

# Ejercicio 5.10
def imprime_primos_hasta(n):
    '''Imprime todos los numeros primos hasta n'''
    for i in range(1, n+1):
        if es_primo(i):
            print(i)

# Ejercicio 5.11, no entendi el enunciado, preguntar
            
# Ejercicio 5.12

def aprobo_o_no(cantidad_ejercicios_examen,porcentaje_necesario):
    cantidad_de_ejercicios_resueltos = 0 # va a ser el centinela
    while cantidad_de_ejercicios_resueltos >= 0:
        cantidad_de_ejercicios_resueltos = int(input('Ingrese la cantidad de ejercicios resueltos correctamente (o un numero negativo si no hay mas examenes a corregir): '))
        if cantidad_de_ejercicios_resueltos >= 0 and cantidad_de_ejercicios_resueltos <= cantidad_ejercicios_examen:
            porcentaje_OK = cantidad_de_ejercicios_resueltos / cantidad_ejercicios_examen * 100
            porcentaje_OK_str = str(porcentaje_OK)
            porcentaje_OK_str_redondeado = porcentaje_OK_str[0:5]
            print('El alumno resolvio correctamente el ' + porcentaje_OK_str_redondeado + '% del examen')
            if porcentaje_OK >= porcentaje_necesario:
                print('El alumno aprobo')
            else:
                print('El alumno no aprobo')
        elif cantidad_de_ejercicios_resueltos > cantidad_ejercicios_examen:
            print('Cantidad de ejercicios incorrecta, o el alumno resolvio correctamente mas ejercicios que los que tenia el examen (neeeerd)')
            
# Ejercicio 6.1

def imprime_dos_primeros_caracteres(s):
    print(s[:2])
    
def imprime_tres_ultimos_caracteres(s):
    print(s[-3:])

def imprime_cada_dos_caracteres(s):
    print(s[0:len(s)+1:2])
    
def imprime_en_sentido_inverso(s):
    print(s[::-1])
    
def imprime_normal_e_inverso(s):
    print(s + s[::-1])
    
def intercala_caracter(s, c):
    sc = ''
    for i in s:
        sc += i
        sc += c
    return sc

# Ejercicio 6.2

def reemplaza_espacios(s, c):
    '''Reemplaza todos los espacios en la cadena s por el caracter c'''
    sc = ''
    for i in s:
        if i == ' ':
            sc += c
        else:
            sc += i
    return sc
    
def reemplaza_digitos(s, c):
    '''Reemplaza todos los digitos en la cadena s por el caracter c'''
    sc = ''
    for i in s:
        if i in '0123456789':
            sc += c
        else:
            sc += i
    return sc

def inserta_cada_tres_digitos(s, c):
    sc = ''
    contador_digitos = 0
    for i in s:
        if i in '0123456789': # no queda claro si se pide esto. por el ejemplo pareciera que s quizas consista solamente de digitos
            contador_digitos += 1
            sc += i
            if contador_digitos % 3 == 0:
                sc += c
        else:
            sc += i
    return sc

# Ejercicio 6.3
    
def intercala_caracter_con_limite(s, c, lim):
    sc = ''
    veces_intercalado = 0
    for i in s:
        sc += i
        if veces_intercalado < lim:
            sc += c
            veces_intercalado += 1
    return sc

def reemplaza_espacios_con_limite(s, c, lim):
    '''Reemplaza todos los espacios en la cadena s por el caracter c, hasta un máximo de lim reemplazos'''
    sc = ''
    cantidad_de_reemplazos = 0
    for i in s:
        if i == ' ' and cantidad_de_reemplazos < lim:
            sc += c
            cantidad_de_reemplazos += 1
        else:
            sc += i
    return sc
    
def reemplaza_digitos_con_limite(s, c, lim):
    '''Reemplaza todos los digitos en la cadena s por el caracter c, hasta un máximo de lim reemplazos'''
    sc = ''
    cantidad_de_reemplazos = 0
    for i in s:
        if i in '0123456789' and cantidad_de_reemplazos < lim:
            sc += c
            cantidad_de_reemplazos += 1
        else:
            sc += i
    return sc

def inserta_cada_tres_digitos_con_limite(s, c, lim):
    sc = ''
    contador_digitos = 0
    cantidad_de_inserciones = 0
    for i in s:
        if i in '0123456789': # no queda claro si se pide esto. por el ejemplo pareciera que s quizas consista solamente de digitos
            contador_digitos += 1
            sc += i
            if contador_digitos % 3 == 0 and cantidad_de_inserciones < lim:
                sc += c
                cantidad_de_inserciones += 1
        else:
            sc += i
    return sc

def agregar_separadores_de_miles(n):
    N = '' # va a contener al número con separadores 
    n = n[::-1] # doy vuelta el numero
    contador_posiciones = 0
    for c in n:
        N += c
        contador_posiciones += 1
        if contador_posiciones % 3 == 0 and contador_posiciones < len(n):
            N += '.'
    return N[::-1]

# Ejercicio 6.5a

def primera_letra_de_cada_palabra(s):
    if s == '':
        return s
    if s[0] != ' ': # si empieza por algo distinto de espacio, la respusta empieza por ese caracter
        primeras_letras = s[0]
    else:
        primeras_letras = '' # si empieza por espacio, la respuesta no va a empezar por espacio
    
    for i in range(len(s)):
        if s[i] == ' ' and i < len(s) - 1:
            primeras_letras += s[i + 1]
    
    return primeras_letras

# Ejercicio 6.5b

def mayusculas_en_cada_palabra(s):
    S = ''
    if s == '':
        return s
    S += s[0].upper()
    for i in range(1,len(s)):
        if s[i-1] == ' ':
            S += s[i].upper()
        else:
            S += s[i]
    return S

# Ejercicio 6.5c

def solo_palabras_que_empiecen_con(s, primera_letra):
    frase = ''
    palabra = ''
    for i in range(len(s)):
        if s[i] == ' ':
            if palabra[0] == primera_letra.lower() or palabra[0] == primera_letra.upper():
                frase = frase + palabra + ' '
                palabra = ''
        elif i == len(s) - 1:
            if palabra[0] == primera_letra.lower() or palabra[0] == primera_letra.upper():
                frase = frase + palabra + s[i]
        else:
            palabra += s[i]
    if frase[-1:] == ' ':
        frase = frase[:-1]

    return frase
        

# Ejercicio 6.6
    
def solo_consonantes(s):
    s_consonantes = ''
    vocales = 'aeiouAEIOU'
    for c in s:
        if c not in vocales:
            s_consonantes += c
    return s_consonantes

    
def solo_vocales(s):
    s_vocales = ''
    vocales = 'aeiouAEIOU '
    for c in s:
        if c in vocales:
            s_vocales += c
    return s_vocales

def reemplaza_vocales(s):
    s_vocalesreemplazadas = ''
    #vocales_minuscula = ('a', 'e', 'i', 'o', 'u', 'a')
    #vocales_mayuscula = ('A', 'E', 'I', 'O', 'U', 'A')
    vocales = 'aeiouaAEIOUA'
    for c in s:
        if c not in vocales:
            s_vocalesreemplazadas += c
        else:
            cont = 0
            while cont < 11:
                if c == vocales[cont]:
                    s_vocalesreemplazadas += vocales[cont + 1]
                    break
                else:
                    cont += 1
    return s_vocalesreemplazadas

def es_palindromo(s):
    s_sinespacios = ''
    for c in s:
        if c != ' ':
            s_sinespacios += c
    if s_sinespacios == s_sinespacios[::-1]:
        return True # asi como está es case-sensitive, o sea devolvería False para 'Anita lava la tina' y True para 'anita lava la tina'
    return False

def pedir_entero(mensaje, minimo, maximo):
    caracteres_posibles = '1234567890'
    numero_negativo = False
    es_entero = True
    while True:
        entrada = input(mensaje + ' ' + f'[{minimo} .. {maximo}]')
        if entrada[0:] == '-': # numero negativo
            entrada = entrada[1:] # me quedo con el resto del caracter, seria el numero positivo
            numero_negativo = True
        for c in entrada:
            if c not in caracteres_posibles:
                es_entero = False
                break # no hay necesidad de seguir iterando si ya se que no es un numero
            es_entero = True # va a perdurar solamente si todos los caracteres son numericos (salvo el primero que ya me lo saque de encima), porque si hay alguno que no lo es, no llega a esta linea por el break
        if es_entero:
            if numero_negativo:
                num = -int(entrada)
            else:
                num = int(entrada)
            if num >= minimo and num <= maximo:
                return num # automaticamente sale del while True
        print(f'Por favor ingrese un número entre {minimo} y {maximo}')
                
            
