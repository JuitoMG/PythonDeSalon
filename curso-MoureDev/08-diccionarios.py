# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.

diccionario = {"name":"Juan","age":40,"country":"Spain"}
print(diccionario)

# 2. Accede al valor de la clave name en el diccionario.
print(diccionario["name"])

# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
diccionario["job"] = "Programador"
print(diccionario)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
diccionario["age"] = 38
print(diccionario)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del diccionario["country"]
print(diccionario)

# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
cuadrados = {x: x**2 for x in range(1,6)}
print(cuadrados)

# 7. Verifica si la clave age está presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
name = {"name": "Brais", "age": 37, "country": "Galicia"}
print("age" in name)

# 8. Imprime solo las claves del diccionario.
print(name.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
listaValores = list(name.keys())
print(listaValores)

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las 
# claves el valor "Desconocido".

mi_lista = ["name", "age", "job"]
diccio_nuevo = {}
diccio_nuevo = diccio_nuevo.fromkeys(mi_lista,"Desconocido")
print(diccio_nuevo)



