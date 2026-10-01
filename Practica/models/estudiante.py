# Importar la clase Persona desde la carpeta 'models', luedo con '.' se accede a la carpeta de la clase superior
from models.persona import Persona

class Estudiante(Persona):
    def __init__(self, id_estudiante, id_persona, nombre, edad, curso):
        super().__init__(id_persona, nombre, edad)
        self.id_estudiante = id_estudiante
        self.curso = curso

    def mostrar_curso(self):
        # Para llamar el metodo de una clase superior
        mensaje = super().presentarse()
        return f'El estudiante: {mensaje}, curso: {self.curso}'

# estudiante1 = Estudiante(1, 1,'Ana', 24, 'A2')
# print(estudiante1.mostrar_curso())
