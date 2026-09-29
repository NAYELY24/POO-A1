class Persona:
    def __init__(self, id_persona, nombre, edad):
        self.id_persona = id_persona
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f'Persona {self.id_persona} {self.nombre} {self.edad} edad'

#persona1 = Persona('09999', 'Luis', '18')
#print(persona1.presentarse())

