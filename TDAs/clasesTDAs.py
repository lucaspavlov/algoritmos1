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
        else:
            while act is not None and act.dato != x:
                ant = act
                act = ant.prox
            if act is not None:
                ant.prox = act.prox
            else:
                raise ValueError('x no aparece en la lista enlazada.')

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
