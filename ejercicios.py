def pedir_entero(mensaje, minimo, maximo):
    caracteres_posibles = '1234567890'
    numero_negativo = False
    es_entero = True
    while True:
        entrada = input(mensaje + ' ' + f'[{minimo} .. {maximo}] ')
        if entrada[:1] == '-': # numero negativo
            entrada = entrada[1:] # me quedo con el resto de la cadena, seria el modulo del numero (si la cadena "es un número")
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
