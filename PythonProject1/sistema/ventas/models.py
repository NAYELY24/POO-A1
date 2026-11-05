from django.db import models

# Create your models here.
# SE VAN A COLOCAR LAS CLASES TAMBIEN CONOCIDAS COMO CLASES-ENTIDADES-MODELOS

# SE REQUIERE CREAR LA CLASE PRODUCTO
class Producto(models.Model):
    # Definir atributos:
    nombre = models.CharField(max_length=10)
    # CUANDO SE REQUIERE AÑADIR ATRIBUTOS A UNA CLASE YA EXISTENTE, DEBEMOS UTILIZAR BLANK Y NULL
    # Blank = True - se activa cuando queremos colocar campos que no sean obligatorios de llenar por el usuario
    # Blank = False- se activa cuando queremos colocar campos que sean OBLIGATORIOS de llenar por el usuario
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(default=0, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True, null=True)

    def __str__(self):
        return f'{self.nombre} - {self.stock}



