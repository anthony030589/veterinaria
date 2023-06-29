from .Conexion import Conexion
from tkinter import messagebox

def GuardarDatosMascota(Mascota):
    conexion = Conexion()
    sql = f"""INSERT INTO Mascota (Nombre, NumeroMicroChip, Especie, Sexo, Tamano, Raza, Color, Edad, 
            FechaNacimiento, Antecedentes) VALUES ('{Mascota.Nombre}',{Mascota.NumeroMicroChip},
            '{Mascota.Especie}','{Mascota.Sexo}','{Mascota.Tamano}','{Mascota.Raza}','{Mascota.Color}',
            {Mascota.Edad},'{Mascota.FechaNacimiento}','{Mascota.Antecedentes}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Mascota'
        mensaje = 'Mascota Registrada Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registrar Mascota'
        mensaje = 'Error al Registrar Mascota'
        messagebox.showerror(title, mensaje)

class Mascota:
    def __init__(self, Nombre, NumeroMicroChip, Especie, Sexo, Tamano, Raza, Color, Edad, FechaNacimiento, Antecedentes):
        self.idMascota = None
        self.Nombre = Nombre
        self.NumeroMicroChip = NumeroMicroChip
        self.Especie = Especie
        self.Sexo = Sexo
        self.Tamano = Tamano
        self.Raza = Raza
        self.Color = Color
        self.Edad = Edad
        self.FechaNacimiento = FechaNacimiento
        self.Antecedentes = Antecedentes

    def __str__(self):
        return f'Mascota[{self.Nombre},{self.NumeroMicroChip},{self.Especie},{self.Sexo},{self.Tamano},{self.Raza},{self.Color},{self.Edad},{self.FechaNacimiento},{self.Antecedentes}]'