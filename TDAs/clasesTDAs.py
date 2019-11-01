class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.cant = 0

    def append(self, dato):
        nuevo = _Nodo(dato, None)
        if self.prim is None:
            self.prim = nuevo
        else:
            act = self.prim
            while act.prox is not None:
                act = act.prox
            act.prox = nuevo
        self.cant += 1

    def pop(self, i = None):
        '''
        Elimina y devuelve el elemento de la posicion i-esima. Si i esta fuera
        de rango devuelve un error. Si no se le pasa un parametro i,
        elimina el ultimo elemento y lo devuelve.
        '''

        if i is None:
            i = self.cant - 1

        if i < 0 or i >= self.cant:
            raise IndexError('Indice fuera de rango.')

        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            act = self.prim
            for k in range(1, i):
                act = act.prox
            dato = act.prox.dato
            act.prox = act.prox.prox

        self.cant -= 1
        return dato

    def remove(self, x):
        '''
        Elimina la primera aparicion de x en la lista enlazada.
        Levanta un error si x no aparece.
        '''
        act = self.prim
        if act is None:
            raise ValueError('Lista vacia.')
        if act.dato == x:
            self.prim = self.prim.prox
            self.cant -= 1
        else:
            while act is not None and act.dato != x:
                ant = act
                act = ant.prox
            if act is not None:
                ant.prox = act.prox
                self.cant -= 1
            else:
                raise ValueError('x no aparece en la lista enlazada.')

    def extend(self, LE):
        '''
        Agrega a una lista enlazada los elementos
        de otra lista enlazada LE que se le pasa por parametro
        '''

        if self.cant != 0:

            act = self.prim
            while act is not None:
                ant = act
                act = act.prox
        
            act_2 = LE.prim
            act = ant
            while act_2 is not None:
                act.prox = act_2
                act_2 = act_2.prox
                act = act.prox
                act.prox = None
                self.cant += 1
           # TERMINAR!

    def filter(self, f):
        L2 = ListaEnlazada()
        act = self.prim
        while act is not None:
            if f(act):
                if L2.cant == 0:
                    act_2 = act
                    L2.prim = act_2
                else:
                    act_2.prox = act
                    act_2 = act_2.prox
                L2.cant += 1
            act = act.prox
            if L2.cant != 0:
                act_2.prox = None
        return L2

    def duplicar(self, elemento):
        len_inicial = self.cant
        if len_inicial == 0:
            raise ValueError('La lista esta vacía')
        act = self.prim
        while act is not None:
            if act.dato == elemento:
                act.prox = _Nodo(elemento, act.prox)
                self.cant += 1
                act = act.prox.prox
            else:
                act = act.prox
        return self.cant - len_inicial

    def __str__(self):
        s = "LE("
        act = self.prim
        while act is not None:
            s += str(act.dato) + ", "
            act = act.prox
        s += ")"
        return s

    def __len__(self):
        return self.cant


class _Nodo:
    """Representa un nodo con un dato y una referencia
    al sig. nodo"""

    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox

    def __repr__(self):
        return f"Nodo({self.dato}, {self.prox})"
