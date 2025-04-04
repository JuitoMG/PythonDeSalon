# Funciones Lambda

#Funcion cuadrado sin lambda

def cuadrado(numero):
    return numero**2

print(cuadrado(3))

# Funcion cuadrado con lambda

cuadrado_lambda = lambda x: x ** 2  #Se asigna la función de la derecha en la variable de la izquierda
print(cuadrado_lambda(3))