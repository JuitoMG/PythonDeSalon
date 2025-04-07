print('*** Manejo de expecciones ***')

def dividir(numerador,denominador):
    try:
        resultado = numerador/denominador
        print(f'Resuldado de dividir {numerador} entre {denominador}: {resultado}')
    except ZeroDivisionError:
        print('Error: No se puede dividir entre cero')  
    except TypeError:
        print('Error: Los operandos deben ser numéricos')          
    except Exception as e:
        print(f'Error: {e}')    

    finally:
        print('Fin del programa')    

dividir(3,2)
dividir(1,7)
dividir(6,2)
dividir(10,0)
dividir(10,'0')

