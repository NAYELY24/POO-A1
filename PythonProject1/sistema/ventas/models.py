from django.db import models

# Create your models here.
# SE VAN A COLOCAR LAS CLASES TAMBIEN CONOCIDAS COMO CLASES-ENTIDADES-MODELOS

# SE REQUIERE CREAR LA CLASE PRODUCTO
class Producto(models.Model):
    # Definir atributos:
    nombre = models.CharField(max_length=10)



