import os

class ServicioPeliculas:

    dir = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(dir,'peliculas.txt')

    def __init__(self):
        self.nombre_archivo = self.ruta

    def agregar_pelicula(self,pelicula):
        with open(self.nombre_archivo, 'a',encoding = 'utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    def listar_peliculas(self):
        with open(self.nombre_archivo, 'r',encoding = 'utf8') as archivo:
            print('--- Listado de películas ---')
            print(archivo.read())     

    def eliminar_archivo(self):
        os.remove(self.nombre_archivo)
        print(f'Archivo eliminado: {self.nombre_archivo}\n')           