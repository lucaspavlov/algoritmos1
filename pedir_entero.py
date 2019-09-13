def pedir_entero(mensaje, minimo, maximo):
    '''Función que pide al usuario un entero entre un valor mínimo y otro máximo (inclusive). Si el usuario ingresa un número que no cumpla eso, o una cadena representando cualquier otra cosa, vuelve a pedir el número. Cuando el usuario ingresa un número entero entre el mínimo y el máximo, la función devuelve ese número'''
    
    caracteres_posibles = '1234567890' # son los caracteres por los que está compuesto un número entero positivo
    
    while True: # repito el loop infinitamente, voy a salir solamente cuando se cumplan las condiciones que pide el enunciado, usando return
        es_entero = True # booleano que es True si el número ingresado es entero o False si no lo es
        es_negativo = False # booleano que va a ser True si el número ingresado es negativo o False si no lo es
        entrada = input(mensaje + ' ' + f'[{minimo} .. {maximo}] ') # imprimo el mensaje para el usuario
        
        if entrada[:1] == '-': # si el primer dígito de la cadena que ingresó el usuario es '-', entonces si lo que se ingresó es un número, es negativo
            entrada = entrada[1:] # me quedo con el resto de la cadena, seria el modulo del numero (si la cadena "es un número")
            es_negativo = True # acá guardo la información de que el número en realidad es negativo, aunque ahora la variable "entrada" sea una cadena que contiene solamente al módulo del número
        
        for c in entrada: # recorro todos los caracteres de "entrada"
            if c not in caracteres_posibles:
                es_entero = False # si algún caracter de "entrada" no es numérico, entonces "entrada" no representa un número entero
                break # esta linea no es estrictamente necesaria, pero no hay necesidad de seguir iterando si ya se que no es un entero. sin la linea funciona igual, porque es_entero nunca va a volver a ser True una vez que ya lo setee como False, pero hace más iteraciones que las necesarias
        
        if es_entero:
            if es_negativo:
                num = -int(entrada) # si la cadena representa un número entero y negativo, obtengo el número usando int() sobre "entrada", que contiene el módulo del número, y agregando el signo -
            else:
                num = int(entrada) # en este caso (es_entero = True y numero_negativo = False) se trata de un entero positivo
            if num >= minimo and num <= maximo:
                return num # si la entrada del usuario representa un número que es entero y está dentro de los valores mínimo y máximo, la función devuelve el número (y con return salgo del while True:)
        
        print(f'Por favor ingrese un número entre {minimo} y {maximo}') # a esta línea se llega si la cadena ingresada no representa un entero entre minimo y maximo. En ese caso se despliega este mensaje y se vuelve a la primera línea del while
