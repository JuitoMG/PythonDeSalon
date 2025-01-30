# 1. Crea una función llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola,
# <nombre>". Si no se proporciona ningún nombre, debe saludar diciendo "Hola, desconocido".

def personalized_greeting (nombre = "Desconocido"):
    print(f"Hola {nombre}")

personalized_greeting("Fulano")


# 2. Escribe una función llamada "multiply" que reciba dos números como argumentos y retorne el resultado de
# multiplicarlos.

def multiply (num1, num2):
    resultado = num1*num2
    return resultado
print(multiply(2,4))

# 3. Crea una función llamada "is_even" que reciba un número entero como argumento y retorne True si es par y False
# si es impar.

def is_even (num):
    if num%2 == 0:
        return True
    else:
        return False
print(is_even(7))    

# 4. Escribe una función llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayúsculas.

def convert_to_uppercase (cadena):
    cadena_mayusculas = cadena.upper()
    return cadena_mayusculas
print(convert_to_uppercase("hola que tal como estas"))


# 5. Crea una función llamada "arbitrary_sum" que reciba un número arbitrario de números como argumentos y retorne
# la suma de todos ellos.

def arbitrary_sum (*numeros):
    suma = sum(numeros)
    return suma
print(arbitrary_sum(1,3,2,5))

# 6. Escribe una función llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el
# saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.

def generate_full_greeting (nombre, apellido):
    print(f"Hola, {nombre} {apellido}")

generate_full_greeting("Fulanez", "Menganez")

# 7. Crea una función llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la
# base al exponente.

def power (base,exponente):
    return base**exponente
print(power(2,3))

# 8. Escribe una función llamada "calculate_average" que reciba tres números y retorne su promedio.

def calculate_average (num1, num2, num3):
    return (num1+num2+num3)/3
print(calculate_average(6,2,1))

# 9. Crea una función llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres
# que contiene.

def count_characters (cadena = ""):
    return len(cadena)
print(count_characters("Trece"))


# 10. Escribe una función llamada "display_messages" que reciba un número indefinido de cadenas y las imprima en
# mayúsculas, una por una, tal como se hizo en el archivo proporcionado.

def display_messages(*texto):
   for i in texto:
       print(i.upper())
    

display_messages("Uno","Dos","Tres")        

