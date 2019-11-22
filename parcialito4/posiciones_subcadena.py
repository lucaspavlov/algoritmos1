def posiciones_subcadena(cadena, subcadena):
    return _posiciones_subcadena(cadena, subcadena, 0)

def _posiciones_subcadena(cadena, subcadena, i):
    L = len(subcadena)
    if i + L > len(cadena):
        return []
    if cadena[i : i + L] == subcadena:
        return [i] + _posiciones_subcadena(cadena, subcadena, i + 1)
    return _posiciones_subcadena(cadena, subcadena, i + 1)
