from django.db import models

# Create your models here.
class Estudiante(models.Model):
    CARRERAS = (
        (1, 'SISTEMA'),
        (2, 'INDUSTRIAL'),
        (3, 'CIVIL'),
        (4, 'ADMINISTRACION'),
        (5, 'MEDICINA'),
        (6, 'OTROS'),
    )
    ESTADOS=[(True,'ACTIVO'),(False, 'INACTIVO')]

    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, blank=True, null=True)
    edad = models.IntegerField(default=0, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    estado = models.BooleanField(choices=ESTADOS, default=True, null=True)
    carrera = models.IntegerField(choices=CARRERAS, null=True)

    def __str__(self):
        return f'{self.nombre}'
