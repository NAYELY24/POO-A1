from django.db import models

# Create your models here.
#SE VAN A COLOCAR LAS CLASES-ENTIDADES-MODELOS

#Se requiere crear la clase producto.
class Producto(models.Model):
    CATEGORIAS = [(1,"Tecnologías"),(2,"Hogar"),(3,"Alimentos"),(4,"Vestimenta"),(5,"Otros"),
                  (6,"Carnes"),]
    #Definir atributos
    nombre = models.CharField(max_length= 10)
    #CUANDO SE REQUIERA AÑADIR ATRIBUTOS A UNA CLASE YA EXISTENTE, DEBEMOS UTILIZAR BLANK y NULL
    #blank = true - Se activa cuando queremos colocar campos que no sean obligatorios de llenar
    # para el usuario
    precio = models.DecimalField(max_digits=10, decimal_places= 2, blank= True, null= True)
    stock = models.IntegerField(default=0, blank= True, null= True)
    descripcion = models.TextField(null=True)
    estado = models.BooleanField(default=True)
    ##SE REQUIERE CREAR UN CAMPO LLAMADO CATEGORIAS PARA SELECCIONAR EL TIPO DE PRODUCTO
    # REGISTRADO, UTILICE ELECCION/CHOICES
    categoria = models.IntegerField(choices=CATEGORIAS, null= True, blank= True)
    def __str__(self):
        return f"{self.nombre} - {self.stock}"


