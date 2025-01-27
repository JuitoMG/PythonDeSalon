# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.

numero = 15

if numero < 0:
    print("Negativo")
else:
    if numero == 0:
        print("Cero")
    else: print("Positivo")

   

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.

edad = int(input("Ingresa tu edad\n"))

if edad < 18:
    print("Menor de edad")
else:
    print("Mayor de edad")


# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.

cadena = ""

if cadena:
     print("La cadena no está vacía")

# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.

numero1 = input("Introduce el primer número\n")
numero2 = input("Introduce el segundo número\n")

if numero1 < numero2:
    print("El segundo número es mayor que el primero")
elif numero1>numero2:
        print("El primer número es mayor que el segundo")
else: 
        print("Los dos números son iguales")

# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.


# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.


# 7. Escribe un programa que determine si una persona puedevotar en función de su edad(mayor o igual a 18). Si tiene 16 o 17 años, indica 
# que puede votar con permisoespecial.


# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida.
# Si no coincide, muestra un mensaje de error.


# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).


# 10. Escribe un programa que simule un semáforo:solicita al usuario que ingrese un color(rojo, amarillo,verde) y muestra un mensaje 
# indicando si debe detenerse, estar alerta o avanzar.