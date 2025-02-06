# 1. Crea un módulo llamado "calculator" que contenga funciones para sumar, restar, multiplicar y dividir dos números.
# Importa este módulo en otro archivo y usa sus funciones.

import module

module.operaciones(3,4)


# 2. Crea un módulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit.
# Escribe un programa que importe este módulo y realice conversiones.

from module import converter

converter(4)
converter(30)
converter(60)

# 3. Crea un módulo que contenga una lista de nombres de estudiantes y una función que imprima todos los nombres.
# Importa este módulo en otro archivo y usa la función para mostrar la lista.

from module import lista_estudiantes

lista_estudiantes()


# 4. Crea un módulo llamado "geometry" que tenga una función para calcular el área de un círculo y un cuadrado. Usa
# este módulo en otro archivo para calcular áreas.

from module import geometry

geometry(2)
geometry(7)
geometry(10)



# 5. Escribe un módulo que contenga una función que acepte cualquier número de argumentos y devuelva su suma. Importa
# y usa la función en otro archivo.

from module import sumar

sumar(3,2,5,6,3,7,7)
sumar("4","20","3","4","5")

# 6. Crea un módulo que defina una clase llamada "Car" con propiedades como marca, modelo y año. Importa este módulo
# en otro archivo y crea una instancia de la clase "Car".

from module import Car

coche = Car("Seat","Ibiza","2009")
coche.datos()

# 7. Escribe un módulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use
# estas funciones para escribir y leer datos.


# 8. Crea un módulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de
# números. Usa este módulo para calcular estos valores en una lista dada.


# 9. Crea un módulo que contenga una función para contar cuántas veces aparece una palabra en un texto. Escribe un
# programa que importe el módulo y lo use para contar palabras en una cadena.


# 10. Crea un módulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia
# entre dos fechas. Usa este módulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas
# específicas.