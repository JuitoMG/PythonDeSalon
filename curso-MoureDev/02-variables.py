# 1. Declara y asigna valores a las siguientes variables:
# name: una cadena que contenga tu nombre.
# age: un número entero que represente tu edad.
# height: un número flotante que represente tu altura.
# Imprime cada variable en una línea separada.

name = "Juan"
age = 33
height = 1.65

print(name,"\n",age,"\n",height)
print(f"")

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuántos años tienes.

edad_string = str(age)
print("Tengo",edad_string,"años")


# 3. Declara una variable booleana is_student que indique si eres estudiante o no. 
# Usa True o False según corresponda e imprímela.

is_student = True
print(is_student)

# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.

nombre_completo = "Fulanez Menganez Citranez"
print(len(nombre_completo))

# 5. Declara tres variables en una sola línea que representen tu nombre, apellido y ciudad de origen. 
# Luego, imprime estos valores.

nomb,ape,ciu = "Fulanez", "Menganez","Vigo"
print(nomb,ape,ciu)

# 6. Usa la función input() para solicitar al usuario su color favorito y almacénalo en una variable color. 
# Luego, imprime el valor ingresado.

color = input("Cual es tu color favorito?")
print(color)

# 7. Declara una variable fruit e inicialízala con un valor. 
# Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.

fruit = "platano"
fruit = "pera"
print(fruit)

# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprímelo.

price = 3.0
print(int(price))

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección usando 
# la función len(). Imprime el resultado.

adress_len = len("Calle de la Silla Enquistada Nº24 3ºA")
print(adress_len)

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un 
# número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().

phone = 3456
phone = 6543
print(type(phone))
