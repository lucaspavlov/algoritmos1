def pedir_entero(mensaje, minimo, maximo):
    '''Función que pide al usuario un entero entre un valor mínimo y otro máximo (inclusive). Si el usuario ingresa un número que no cumpla eso, o una cadena representando cualquier otra cosa, vuelve a pedir el número. Cuando el usuario ingresa un número entero entre el mínimo y el máximo, la función devuelve ese número'''
    # Materia: Algoritmos y Programación 1 cátedra Essaya, práctica Grace. Alumno: Lucas Pavlov, legajo 105412. Correctora: Florencia Rodríguez.

    while True:
        entrada = input(mensaje + ' ' + f'[{minimo} .. {maximo}] ')
        cadena_a_chequear = entrada
        if entrada[:1] == '-': 
            cadena_a_chequear = entrada[1:]
        if cadena_a_chequear.isdigit():
            num = int(entrada)
            if num >= minimo and num <= maximo:
                return num

        print(f'Por favor ingrese un número entre {minimo} y {maximo}')
