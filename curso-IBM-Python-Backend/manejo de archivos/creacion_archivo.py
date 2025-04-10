#Creación archivo

nombre_archivo = 'mi_archivo.txt'

# Abrimos archivo y escribimos en él

archivo = open(nombre_archivo,'w')
archivo.write('Hola, cómo estás')
archivo.write('\nPor aquí...')
archivo.close()

print(f'Se creó el archivo: {nombre_archivo}')

# Otro método más simple

with open(nombre_archivo,'w') as archivo:
    archivo.write('Hola, cómo estás 2')
    archivo.write('\nPor aquí vamos...')
