from maquina_snacks_proyecto.servicio_snacks import ServicioSnacks


class MaquinaSnacks:
    def __init__(self):
        self.servicio_snacks = ServicioSnacks()
        self.productos = []

    def maquina_snacks(self):
        salir = False
        print('--- Máquina de Snacks ---\n')
        self.servicio_snacks.mostrar_snacks()    