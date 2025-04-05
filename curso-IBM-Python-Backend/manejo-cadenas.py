# manejo cadenas

# Dividir cadenas split() (parsing)

cadena = 'Hola Mundo'
palabras = cadena.split('M')
print(palabras)

# Find y replace
posicion = cadena.find('Mundo')
print(f'Posicion de la cadena Mundo: {posicion}')

nueva_cadena = cadena.replace('Mundo','Amigo')
print(nueva_cadena)

#Funcion Strip elilima caracteres en blanco

cadena = '   Hola Mundo      '
cadena_limpia = cadena.strip()
print(cadena_limpia)
cadena = '.....Hola Mundo.....'
cadena_limpia = cadena.strip('.')
print(cadena_limpia)


