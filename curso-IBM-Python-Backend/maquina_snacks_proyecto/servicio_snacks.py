import os.path
from maquina_snacks_proyecto.snack import Snack

class ServicioSnacks:
    NOMBRE_ARCHIVO = 'snacks.txt'

    def __init__(self):
        self.snacks = []

        # Revisar si existe el archivo para mostrar la lista
        # Si no existe, se cargará uno con snacks iniciales

        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.snacks = self.obtener_snacks()
        else:
            self.cargar_snacks_iniciales()   


    def cargar_snacks_iniciales(self):
        snacks_iniciales = [
            Snack('Patatas',2),
            Snack('Refresco',3),
            Snack('Galletas',2)
        ]         
        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)

    def guardar_snacks_archivo(self,snacks):
        try:
            with open(self.NOMBRE_ARCHIVO,'a') as archivo:
                for snack in snacks:
                    archivo.write(f'{snack.escribir_snack()}\n')
        except Exception as e:
            print(f'Error al guardar el archivo: {e}')        

    def obtener_snacks(self):
        snacks = []

        try:
            with open(self.NOMBRE_ARCHIVO,'r') as archivo:
                for linea in archivo:
                    id_snack, nombre, precio = linea.strip().split((',')) # Evita espacios en blanco y genera una tupla metiendo el valor de cada línea en la variable correspondiente
                    snack = Snack(nombre, float(precio))
                    snacks.append(snack)

        except Exception as e:
            print(f'Error al leer archivo de snacks: {e}')    
        return snacks  

    def agregar_snack(self,snack):
        self.snacks.append(snack)
        self.guardar_snacks_archivo([snack])  

    def mostrar_snacks(self):
        print('--- Lista de Snacks en el inventario ---\n')
        for snack in self.snacks:
            print(snack)    

    def get_snacks(self):
        return self.snacks        
