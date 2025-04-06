# Decoradores - Una funcion dentro de una funcion


def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Antes de saludar")
        resultado = funcion(*args, **kwargs) # Llamamos a nuestra función
        print('Despues de llamar la funcion saludar')
        return resultado
    return wrapper

@decorador
def saludar(nombre):
    print(f'Hola {nombre}')

saludar('Paco')