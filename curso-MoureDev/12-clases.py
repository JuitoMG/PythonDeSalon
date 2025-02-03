# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un método "make_sound" que imprima un sonido genérico.

class Animal:
    def __init__(self,species):
        self.species = species
    def make_sound (self):
        print("Ñiiiiiaaaaaakkkk")    

animal = Animal("Mono")
print(animal.species)

animal.make_sound()

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacénala en una propiedad pública.
# Añade el método "make_sound" que imprima un sonido dependiendo de la especie.

class Animal:
    def __init__(self,species):
        self.species = species
    def make_sound (self):
        if self.species == "Mono":
            print("Kikikiki kaaaaaa")
        elif self.species == "Aguila":
            print("Ñiiiiiaaaaaakkkk")
        else:
            print("Animal no identificado")         

animal = Animal("Aguila")
print(animal.species)

animal.make_sound()


# 3. Crea una clase llamada "Car" con las propiedades públicas"brand" y "model". Además, debe tener una propiedad
# privada "_speed" que inicialmente será 0.

class Car:
    def __init__(self, brand, model, speed = 0):
        self.brand = brand
        self.model = model
        self.__speed = speed


# 4. Añade a la clase "Car" un método llamado "accelerate" que aumente la velocidad en 10 unidades. Añade también un
# método "brake" que reduzca la velocidad en 10 unidades. Asegúrate de que la velocidad no sea negativa.

class Car:
    def __init__(self, brand, model, speed = 0):
        self.brand = brand
        self.model = model
        self.__speed = speed

    def accelerate (self):
        self.__speed = self.__speed + 10
        print("+10 de velocidad")

    def brake (self):
        
        if self.__speed <= 9:
            print("No se puede reducir velocidad")
        else:
            self.__speed = self.__speed - 10
            print("-10 de velocidad")    

    def speed (self):
        print("Velocidad: ",self.__speed)

coche = Car("Opel","Corsa",10)
coche.speed()
coche.accelerate()    
coche.speed()
coche.brake()
coche.speed()
coche.brake()  
coche.brake()            

# 5. Crea una clase "Book" que tenga propiedades como "title" (público) y "author" (privado). Añade un método para
# obtener el autor y otro para cambiar el título del libro.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author

    def obtener_autor (self):
        print(self.__author)    

    def cambiar_titulo(self,newTitle):
        self.title = newTitle
        print("Título cambiado")

    def mostrar_info(self):
        print(self.title)
        print(self.__author)       

libro = Book("Piar","Fulano")
libro.obtener_autor()
libro.mostrar_info()
libro.cambiar_titulo("Falafel")
libro.mostrar_info()


# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. Añade un método
# para calcular y devolver la nota media del estudiante.

class Estudiante:
    def __init__(self, nombre, apellido, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = notas

    def media(self):
        return sum(self.notas)/len(self.notas)   

estudiante = Estudiante("Fulanez","Menganez",[3,6,8,4])
print("Nota media de ",estudiante.nombre,":",estudiante.media())



# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade métodos para depositar y retirar
# dinero, asegurándote de que no se pueda retirar más de lo que hay en la cuenta.

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def ingeso(self,ingreso):
        self.ingreso = ingreso
        self.balance = self.balance + self.ingreso
        print("Ingresados ",ingreso,"€. Saldo actual:",self.balance,"€")

    def retirada(self,retiro):
        self.retiro = retiro
        if retiro <= self.balance:
            self.balance = self.balance - self.retiro
            print("Retirados ",retiro,"€. Saldo actual:",self.balance,"€")
        else:
            print("Saldo insuficiente")

cliente = BankAccount("Fulano",300.0)
cliente.ingeso(30)
cliente.retirada(50)
cliente.retirada(400)



# 8. Crea una clase "Point" que represente un punto en elespacio 2D con coordenadas "x" e "y". Añade un método que
# calcule la distancia entre dos puntos.

import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distancia(self):
        distancia = self.x - self.y
        if distancia <0:
            distancia = -distancia
        print("La distancia entre ",self.x,"y",self.y,"es:",distancia)
        
        
punto = Point(4,9)
punto.distancia()        


# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked".
# Añade un método que calcule el pago total basado en las horas trabajadas y el salario por hora.

class Employee:
    def __init__(self,name,hourly_wage,hours_worked):
        self.name = name
        self.hourlt_wage = hourly_wage
        self.hours_worked = hours_worked

    def salario(self):
        salario = self.hourlt_wage * self.hours_worked
        print("Salario de",self.name,":",self.hours_worked,"horas,",self.hourlt_wage,"€/h. Total:",salario,"€")  

empleado = Employee("Fulano",8,245)

empleado.salario()


# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). Añade un método para
# agregar un producto al inventario y otro para mostrar todos los productos disponibles.

class Store:
    def __init__(self):
        self.inventory = []

    def agregar_producto (self,producto):
        self.inventory.append(producto)
        print("Producto agregado")

    def mostrar_inventario(self):
        for i in self.inventory:
            print("-",i) 

tienda = Store()
tienda.agregar_producto("Patatas")
tienda.agregar_producto("Nuecess")
tienda.agregar_producto("Pescado")
tienda.agregar_producto("Caramelos")
tienda.agregar_producto("Leche")
tienda.mostrar_inventario()               

