import vectores

def area_triangulo(x1, y1, x2, y2, x3, y3):
    '''Dados tres puntos en el plano, devuelve el area del triangulo que forman'''
    lado_1_x, lado_1_y, lado_1_z = vectores.diferencia(x1, y1, 0, x2, y2, 0) # calculo el vector que va desde el punto 2 hasta el punto 1
    lado_2_x, lado_2_y, lado_2_z = vectores.diferencia(x1, y1, 0, x3, y3, 0) # calculo el vector que va desde el punto 3 hasta el punto 1
    prodvec_x, prodvec_y, prodvec_z  = vectores.producto_vec(lado_1_x, lado_1_y, lado_1_z, lado_2_x, lado_2_y, lado_2_z) # hago el producto vectorial de los dos vectores anteriores.
    area = vectores.norma(prodvec_x, prodvec_y, prodvec_z) / 2 # La norma del producto vectorial da como resultado el area del paralelogramo generado por los dos vectores calculados con diferencia(), que es el doble del area del triangulo
    return area

# Pruebas para verificar el uso de la funcion
assert area_triangulo(1, 1, 1, 1, 1, 1) == 0 # son el mismo punto
assert area_triangulo(0, 0, 1, 1, 2, 2) == 0 # son colineales (no forman triangulo)
assert area_triangulo(0, 0, 1, 1, 1, 1) == 0 # son dos puntos (no forman triangulo)
assert area_triangulo(5, 3, 5, 4, 7,  3) == 1 # base*altura/2 (base=2, altura=1)
assert area_triangulo(0, 0, 1, 0, 0, 1) == 1/2 # isosceles
assert area_triangulo(0, 0, -1, 0, 0, -1) == 1/2 # idem para el otro lado
assert area_triangulo(-1, 0, 1, 0, 0, 8) == 8
assert area_triangulo(-1, 0, 1, 0, 1, 8) == 8
assert area_triangulo(-1, 0, 1, 0, 1/2, 8) == 8
assert area_triangulo(1/2, 8, 1, 0, -1, 0) == 8
assert area_triangulo(1, 0, 1/2, 8, -1, 0) == 8
