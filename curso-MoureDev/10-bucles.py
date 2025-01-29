# 1. Usa un bucle while para imprimir los números del 1 al 10.

numero=1

while numero < 11:
    print(numero)
    numero += 1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número.

lista = [10, 20, 30, 40, 50]

for i in lista:
    print(i)

# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.

numeros = 0
resultado = 0

while numeros < 101:
    print(resultado,"+",numeros,"=",resultado+numeros)
    resultado = resultado + numeros
    numeros +=1

# 4. Escribe un bucle for que imprima cada carácter de la cadena “Python”.

cadena = "Python"

for i in cadena:
    print(i)

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.

numero = 1

while numero < 50:
    if numero%7 == 0:
        print(numero)
        break
    numero +=1

# 6. Usa un bucle for para recorrer el diccionario {“name”:“Brais”,“age”: 37, “country”: “Galicia”} e imprime las claves.

diccionario = { "name":"Brais","age": 37, "country": "Galicia"}

for i in diccionario:
    print(i)

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.

numero = 1

while numero < 21:
    if numero%2 == 0:
        print(numero)
    numero +=1


# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.

for i in range(20,0,-1):
    print(i)

# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].

lista = [30, 10, 30, 20, 30, 40]
contador = 0

for i in lista:
    if i == 30:
        contador +=1
print("El número 30 aparece",contador,"veces en la lista")        


# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre “Brais”.

lista= ["Fulanez","Menganez","Citranez","Brais","Pepe"]

for i in lista:
    print(i)
    if i == "Brais":
        break