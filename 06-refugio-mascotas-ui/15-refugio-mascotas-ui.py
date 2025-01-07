import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

class RegistroMascotasGUI:

    dir = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(dir,"refugio_mascotas.db")

    def __init__(self, root,nombredb=ruta):

        self.root = root
        self.root.title("Registro de mascotas")
        self.conn = sqlite3.connect(nombredb)
        self.cursor = self.conn.cursor()
        self.crear_tabla()

        self.create_widgets()

    def crear_tabla(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXIST mascotas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                tipo TEXT NOT NULL,
                edad INTEGER NOT NULL,
                estado TEXT NOT NULL CHECK(estado IN('En adopcion','Adoptado'))
            )
        ''')
        self.conn.commit()

    def create_widgets(self):

        tk.Label(self.root, text="Nombre:").grid(row=0, column=0,padx=10,pady=5)
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.grid(row=0,column=1,padx=10,pady=5)

        tk.Label(self.root,text="Tipo:").grid(row=1,column=0,padx=10,pady=5)
        self.entry_tipo = tk.Entry(self.root)
        self.entry_tipo.grid(row=1,column=1,padx=10,pady=5)

        tk.Label(self.root,test="Edad:").grid(row=2,column=0,padx=10,pady=5)
        self.entry_edad = tk.Entry(self.root)
        self.entry_edad.grid(row=2,column=1,padx=10,pady=5)

        tk.Label(self.root,text="Estado:").grid(row=3,column=0,padx=10,pady=5)
        self.entry_estado = tk.Entry(self.root)
        self.entry_estado.grid(row=3, column=1,padx=10,pady=5)

        tk.Button(self.root, text="Registrar Mascota", command=self.agregar_mascota).grid(row=4,column=0,columnspan=2,pady=10)
        tk.Button(self.root, text="Listar Mascotas", command=self.listar_mascotas).grid(row=5,column=0,columnspan=2,pady=10)

    def agregar_mascota(self):
        nombre = self.entry_nombre.get()
        tipo = self.entry_tipo()
        try:
            edad = int(self.entry_edad.get())
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número. ")
            return
        estado = self.entry_estado.get()

        if estado not in ['En adopcion','Adoptado']:
            messagebox.showerror("Error", "El estado debe ser 'En adopcion' o 'Adoptado'.")
            return

        self.cursor.execute('''
            INSERT INTO mascotas (nombre, tipo, edad, estado)
            VALUES (?,?,?,?)
        ''',(nombre,tipo,edad,estado))
        self.conn.commit()
        
                        
        