print('--- Leer archivo ---')

nombre_archivo = 'mi_archivo.txt'

# Leer archivo con ReadLines

with open(nombre_archivo, 'r') as archivo:
    # Leer todas las líneas del archivo
    print(archivo.readlines())

    #Imprimir línea por línea
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea)

    # Con srip se quitan los tabuladores, espacios, saltos de línea, etc
    for linea in lineas:
        print(lineas.strip())    


    # Leer el contenido del archivo usando el método Read    

    print('Leyendo el contenido con el método read')
    with open(nombre_archivo,'r') as archivo:
        print(archivo.read())
