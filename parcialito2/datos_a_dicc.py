#anio, mes, vendedor, cliente, monto

def datos_a_dicc(camino_datos, camino_errores):
	vendedores = {}
    with open(camino_datos) as datos, open(camino_errores, 'a') as errores:
        linea = camino_datos.readline()
        while linea != '':
            try:
                anio, mes, vendedor, cliente, monto = linea.rstrip('\n').split(',')
                if vendedor in vendedores.keys():
                    dicc[vendedor] += float(monto)
                else:
                    dicc[vendedor] = float(monto)
            except:
                errores.write(linea)
            finally:
                linea = camino_datos.readline()

datos_a_dicc('datos.csv', 'errores.csv')
