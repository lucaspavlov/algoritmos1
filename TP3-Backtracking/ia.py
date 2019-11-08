from pila import Pila
from mapa2 import Mapa,Coord

class IA:
    """
    Inteligencia artificial para resolver un laberinto.

    Se simula un jugador que comienza en la celda de origen, y mediante
    el método avanzar() el jugador hace un movimiento.

    Ejemplo:
        >>> mapa = Mapa(10, 10)
        >>> ia = IA()
        >>> ia.coord_jugador()
        Coord(0, 0)
        >>> while ia.coord_jugador() != mapa.destino()
        ...     ia.avanzar()
        >>> ia.coord_jugador()
        Coord(9, 9)
    """

    def __init__(self, mapa):
        """Constructor.

        Argumentos:
            mapa (Mapa): El mapa con el laberinto a resolver
        """
        self.mapa = mapa
        self.posicion = mapa.origen()
        self._visitados = [mapa.origen()]
        self.camino=Pila()

    def coord_jugador(self):
        """Coordenadas del "jugador".

        Devuelve las coordenadas de la celda en la que se encuentra el jugador.

        Devuelve:
            Coord: Coordenadas del "jugador"

        Ejemplo:
            >>> ia = IA(Mapa(10, 10))
            >>> ia.coord_jugador()
            Coord(0, 0)
            >>> ia.avanzar()
            >>> ia.coord_jugador()
            Coord(1, 0)
            >>> ia.avanzar()
            >>> ia.coord_jugador()
            Coord(2, 0)
        """
        return self.posicion

    def visitados(self):
        """Celdas visitadas.

        Devuelve:
            secuencia<Coord>: Devuelve la lista (o cualqueir otra secuencia) de
            de celdas visitadas al menos una vez por el jugador desde que
            comenzó la simulación.

        Ejemplo:
            >>> ia = IA(Mapa(10, 10))
            >>> ia.avanzar()
            >>> ia.avanzar()
            >>> ia.avanzar()
            >>> ia.visitados()
            [Coord(0, 0), Coord(1, 0),  Coord(2, 0)]
        """
        return self._visitados

    def camino(self):
        """Camino principal calculado.

        Devuelve:
            secuencia<Coord>: Devuelve la lista (o cualqueir otra secuencia) de
            de celdas que componen el camino desde el origen hasta la posición
            del jugador. Esta lista debe ser un subconjunto de visitados().

        Ejemplo:
            >>> ia = IA(Mapa(10, 10))
            >>> for i in range(6):
            ...     ia.avanzar()
            >>> ia.visitados()
            [Coord(0, 0), Coord(1, 0), Coord(1, 1),  Coord(2, 0),  Coord(3, 0),  Coord(4, 0)]
            >>> ia.camino()
            [Coord(0, 0), Coord(1, 0),  Coord(2, 0),  Coord(3, 0),  Coord(4, 0)]

        Nota:
            La celda actual en la que está el jugador puede no estar en la
            lista devuelta (esto tal vez permite simplificar la
            implementación).
        """
        return self.camino

    def avanzar(self):
        """Avanza un paso en la simulación.

        Si el jugador no está en la celda destino, y hay algún movimiento
        posible hacia una celda no visitada, se efectúa ese movimiento.
        """
        if self.posicion==self.mapa.destino():
            return
        movimientos_posibles = ((1, 0), (0, 1), (-1, 0), (0, -1))
        anterior=self.posicion
        for movimiento in movimientos_posibles: # de esta forma no es aleatorio porque siempre intenta primero con el (1, 0), etc.
            df, dc = movimiento
            candidato = self.posicion.trasladar(df, dc)
            if candidato not in self.visitados() and self.mapa.es_coord_valida(candidato) and not self.mapa.celda_bloqueada(candidato):
                self.posicion = candidato
                self._visitados.append(candidato) #Si ya no esta en self.visitados lo preguntabas dos veces
                self.camino.apilar(candidato)
        if self.posicion==anterior:
            self.camino.desapilar()
            candidato=self.camino.desapilar()
            self.camino.apilar(candidato)
            self.posicion=candidato

                    


