from catalogo_peliculas.servicio_peliculas import ServicioPeliculas
class AppCatalogoPeliculas:

    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()

    def mostrar_menu(self):
        print('--- App Catálogo Películas ---')
        while True:
            try:
                print(f'''Opciones:
                1. Agregar película
                2. Listar películas
                3. Eliminar catálogo
                4. Salir''')
                opcion = int(input('Escribe tu opción: '))
                if opcion == 1:
                    print('-- Agregar película --\n')
                    nombre_pelicula = input('Escribe el nombre de la película')
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicio_peliculas.agregar_peliculas(pelicula)

                elif opcion == 2:
                    self.servicio_peliculas.listar_peliculas() 

                elif opcion == 3:
                    self.servicio_peliculas.eliminar_archivo()   
                elif opcion == 4:
                    print('Saliendo del programa...')    
                    break
                else:
                    print('Opción inválida: Introduce un valor entre 1 y 4.\n')


            except ValueError:
                print('Error. Introduce un número válido')
            except Exception as e:
                print(f'Error: {e}')        
