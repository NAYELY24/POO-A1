#Ejercicio 1
#Se requiere crear una clase padre "Animal" con los siguientes atributos
#Nombre, edad, peso, color, habitad
#Tambien se requiere crear tres clases hijas:
#Perro, Gato y Vaca.
#Cada clase hija debera tener al menos tres atributos propios.

class Animal:
    def __init__(self, nombre, edad, peso, color, habitat):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.color = color
        self.habitat = habitat

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Peso: {self.peso}, Color: {self.color}, Habitat: {self.habitat}"

# Animal1=Animal("Clifford", 3, 80, "Rojo", "Ciudad")
# Animal2=Animal("Jorge", 2, 3, "Café", "Ciudad")
# print(Animal1.mostrar_info())
# print(Animal2.mostrar_info())
# print(Animal1.nombre)
# print(Animal2.nombre)

class Perro(Animal):
    def __init__(self, nombre, edad, peso, color, habitat, raza, tamano, entrenado):
        super().__init__(nombre, edad, peso, color, habitat)
        self.raza = raza
        self.tamano = tamano
        self.entrenado = entrenado

    def info_perro(self):
        return f"El Nombre del Perro es: {self.nombre}\nSu Edad es: {self.edad}\nPesa: {self.peso} kg\nSu Color es: {self.color}\nSu Habitat es: {self.habitat}\nSu Raza es: {self.raza}\nSu Tamaño es: {self.tamano} cm\n¿Está Entrenado?: {self.entrenado}"

perro1=Perro("Bluey", 7, 15, "Celeste", "Ciudad", "Blue Heeler", 84, True)
print(perro1.info_perro())

class Gato(Animal):
    def __init__(self, nombre, edad, peso, color, habitat, num_vidas, tipo_pelaje, color_ojos):
        super().__init__(nombre, edad, peso, color, habitat)
        self.num_vidas = num_vidas
        self.tipo_pelaje = tipo_pelaje
        self.color_ojos = color_ojos

#Polimorfismo: Muestra lo que deseas en el método 
    def mostrar_info(self):
        return f"El Nombre del Gato es: {self.nombre}\nTiene: {self.num_vidas} vidas\nSu Tipo de Pelaje es: {self.tipo_pelaje}\nSus ojos son color: {self.color_ojos}"

Gato1=Gato("Garfield", 8, 12, "Naranja", "Domestico", 5, "Atigrado", "Negros")
print(Gato1.mostrar_info())
