from django.shortcuts import render
from .models import Persona


def listar_persona(request):
    personas = Persona.objects.filter(estado=True)
    return render(request, 'universidad/listar_persona.html', {'personas': personas})
