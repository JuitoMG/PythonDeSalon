# 1. Crea una función que intente dividir dos números proporcionados por el usuario. Usa try-except para
# capturar cualquier error de división (por ejemplo, división por cero).

def division():
    numero1 = int(input("Introduce el primer número"))
    numero2 = int(input("Introduce el segundo número"))

    try:
        print(numero1 / numero2)
    except:
        print("Se ha producido un error")    

division()

# 2. Crea una función que tome una cadena e intente convertirla en un número entero. Usa try-except para
# capturar cualquier error en la conversión.

def entero (cadena):
    try:
        entero_nuevo = int(cadena)
        print(entero_nuevo)
    except:
        print("Error")

entero(5)
entero("4")
entero("Lavar")        


# 3. Crea una función que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no
# encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.

def leer_archivo(archivo):
    try:
        lectura = open(archivo,"r")
        print(lectura.read())
        lectura.close()
    except FileNotFoundError:
        print("Archivo no encontrado") 

leer_archivo("fichas.doc")           


# 4. Crea una función que realice múltiples operaciones (suma, resta, división, multiplicación) con dos números.
# Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final,
# independientemente de los errores.

def operaciones (num1,num2):
    print("Menú\n")
    print("1. Suma")
    print("2. Resta")
    print("3.Multiplicación")
    print("4.División\n")

    
    try:
        opcion = int(input("Elige una opción\n"))
        if opcion == 1:
            try:
                print(num1,"+",num2,"=",num1+num2)
            except:
                print("Error en la suma")
        elif opcion == 2:
            try:
                print(num1,"-",num2,"=",num1-num2)
            except:
                print("Error en la resta")
        elif opcion == 3:
            try:
                print(num1,"*",num2,"=",num1*num2)
            except:
                print("Error en la multiplicación")
        elif opcion == 4:
            try:
                print(num1,"/",num2,"=",num1/num2)
            except:
                print("Error en la división")
        else:
            print("Opción incorrecta")
    except:
        print("Opción no válida")  
    finally:
        print("Operación realizada correctamente")     

operaciones(2,0)                             
                     


# 5. Crea una función que le pida al usuario su edad y lance un ValueError si la entrada no es un número entero
# positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea
# necesario.
def edad(numero):
    try:
        edad = int(numero)
        print(edad)
    except ValueError:
        print("Error. Número no reconocido")

edad(3)
edad("4")
edad("j")


# 6. Crea una función que intente acceder a un elemento de una lista por índice. Usa try-except para manejar el
# caso donde el índice esté fuera de rango.

lista = [1,2,3,4]

def ver_lista(indice):
    try:
        indice = int(indice)
        print(lista[indice])
    except ValueError:
        print("Número no reconocido")
    except IndexError:
        print("Error IndexError, índice fuera de rango")

ver_lista(2)
ver_lista("2")
ver_lista(8)        
        

# 7. Crea una función que use try-except para manejar múltiples excepciones: ZeroDivisionError, ValueError y TypeError.

def varios_errores(num1, num2):
    try:
        numero1 = int(num1)
        numero2 = int(num2)
        print(num1/num2)
    except ValueError:
        print("Error: ValueError. Valor incorrecto")
    except TypeError:
        print("Error: Tipo de dato no reconocido")
    except ZeroDivisionError:
        print("Error: Número indivisible por 0") 
    else:
        print("Operación correcta")
    finally:
        print("Se sigue con el programa...")            

varios_errores(2,2)
varios_errores("2","3")
varios_errores(2,0)
varios_errores("alfa","beta")

# 8. Crea una función que simule una transacción. Lanza una excepción personalizada llamada InsufficientFundsError
# si el saldo es menor que la cantidad a retirar.

def transaccion(dinero):
    dinero = int(dinero)
    saldo = 100
    try:
        if dinero>saldo:
            raise ValueError("saldo insuficiente")
        else:
            saldo = saldo - dinero
            print("Saldo actual:",saldo)
    except Exception as InsufficientFundsError:
        print("Saldo insuficiente")

transaccion(80)
transaccion(110)        
    

# 9. Crea una función que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja
# cuando una cadena no pueda convertirse.



# 10. Crea una función que calcule la raíz cuadrada de un número. Lanza un ValueError si el número es negativo.