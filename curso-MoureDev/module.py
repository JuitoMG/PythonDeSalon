import math

#operaciones

def operaciones(num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    try:
        resultado = num1+num2
        print(num1,"+",num2,"=",resultado)

        resultado = num1-num2
        print(num1,"-",num2,"=",resultado)

        resultado = num1*num2
        print(num1,"x",num2,"=",resultado)

        resultado = num1/num2
        print(num1,"/",num2,"=",resultado)
    except:
        print("Error")    



#Celsius - Faren

def converter(num):
    num = int(num)
    try:
        celsius = round((5/9)*(num-32),2)
        print(num,"ºF =",celsius,"ºC")
        faren = round((9/5)*(num+32),2)
        print(num,"ºC =",faren,"ºF")
    except:
        print("Error")

#Lista estudiantes

def lista_estudiantes():
    lista = ["Fulanez","Menganez","Citranez"]
    print(lista)

#area círculo y cuadrado

def geometry(num):
    num=int(num)
    try:
        print("El area de un cuadrado de",num,"de lado es",round((num*num),2))
        print("El area de un círculo de",num,"de radio es",round((math.pi*num**2),2))
    except:
        print("Error")    


#Sumar todos los números

def sumar(*num):
    try:
        print(sum(num)) 
    except:
        print("Error")    


#Clase coche

class Car:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def datos (self):
        print(self.marca,self.modelo,self.año)    
