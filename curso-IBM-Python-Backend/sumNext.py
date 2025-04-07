print('*** Función Sum y next ***')

lista = [1,2,3,4,5]

# Suma de todos los elementos
resultado = sum(lista)
print(f'Resultado de la suma: {resultado}')

# Con valor inicial

resultado = sum(lista, 20)
print(f'Resultado de la suma con valor inicial 20: {resultado}')

#Función Next

iterador = iter(lista)

valor = next(iterador)
print(valor)

print(f'Siguiente elemento iterable: {next(iterador)}')