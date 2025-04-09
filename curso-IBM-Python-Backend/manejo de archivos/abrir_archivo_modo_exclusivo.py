print(' -- Abrir archivo en modo exclusivo -- ')

nombre_archivo = 'mi_archivo.txt'
try:
    with open(nombre_archivo, 'x') as archivo:
        archivo.write('Escritura en modo exclusivo')
    print('Se ha creado el archivo')    
except FileExistsError as e:
    print(f'El archivo {nombre_archivo} ya existe.' )    
    print(f'Detalle del error: {e}')