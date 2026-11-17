from django.contrib import admin
from .models import Persona


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombres', 'edad', 'telefono', 'correo', 'estado')
    search_fields = ('cedula', 'nombres')
