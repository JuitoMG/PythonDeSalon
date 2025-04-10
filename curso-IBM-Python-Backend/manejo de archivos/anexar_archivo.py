print('--- Anexar archivo ---')
nombre_archivo = 'mi_archivo.txt'

with open(nombre_archivo, 'a') as archivo:
    #Agregamos información al archivo
    archivo.write('\nAgregando información al archivo.')
    archivo.write('Terminando de agregar información nueva.')

print(f'Se ha agregado información al archivo {nombre_archivo}')