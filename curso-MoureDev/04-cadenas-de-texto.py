# 1. Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.

print("Hola"+"Python")

# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.

print("Esto es\nun salto de línea ")

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
nombre = "Juan"
apellido = "Mar"
edad= 43

print(f"{nombre} {apellido} {edad}")

# 5. Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.
a,b,c,d,e,f = "Python"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6. Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.

palabra = "Programación"
palabra_slice = palabra[3:7]
print(palabra_slice)


# 7. Invierte la cadena “Python” usando slicing y muestra el resultado.
cadena = "Pyhon"
reverse_lenguaje = cadena[::-1]
print(reverse_lenguaje)

# 8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.
cadena2 = "aprendiendo python"
print(cadena2.upper())

# 9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.

cadena3 = "Programación en Python"
print(cadena3.count("n"))

# 10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado

print("12345".isnumeric())