from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models


class Persona(models.Model):
    cedula = models.CharField(
        max_length=10,
        unique=True,
        validators=[RegexValidator(r'^\d{10}$', 'La cédula debe tener 10 dígitos.')],
    )
    nombres = models.CharField(max_length=100)
    edad = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(120)]
    )
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.cedula} - {self.nombres}"
