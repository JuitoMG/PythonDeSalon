class Animal:
    def comer(self):
        print('Como muchas veces al día')

    def dormir(self):
        print('Duermo muchas horas')



class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')


#Programa principal

print('Ejemplo de herencia en Python')
print('Clase Padre, soy un animal')
animal1 = Animal()

animal1.comer()
animal1.dormir()

# Clase hija, soy un perro

print('\nClase hija, soy un perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()