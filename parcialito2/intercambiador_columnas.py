def intercambiador_columnas(col1, col2, path_r, path_w):
    with open(path_r) as archivo_original, open(path_w, 'w') as archivo_final:
        linea = archivo_original.readline()
        while linea != '':
            columnas = linea.rstrip('\n').split(',')
            columnas[col1], columnas[col2] = columnas[col2], columnas[col1]
            linea_final = ','.join(columnas)
            archivo_final.write(linea_final + '\n') # no vale para todo sistema operativo, no?
            linea = archivo_original.readline()

intercambiador_columnas(2,4,'columnas.csv','columnas_intercambiadas.csv')
