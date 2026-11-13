from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import EstudianteForm
from .models import Estudiante


def listar_estudiantes(request):
    # Se muestran todos para poder activar nuevamente a los inactivos.
    estudiantes = Estudiante.objects.all().order_by("id")
    return render(request, "estudiantes/listar_estudiantes.html", {"estudiantes": estudiantes},)


def crear_estudiantes(request):
    if request.method == "POST":
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El estudiante se registró correctamente.")
            return redirect("listar_estudiantes")
    else:
        formulario = EstudianteForm()

    return render(
        request,
        "estudiantes/crear_estudiantes.html",
        {"formulario": formulario},
    )


def editar_estudiantes(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)

    if request.method == "POST":
        formulario = EstudianteForm(request.POST, instance=estudiante)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Los datos del estudiante se actualizaron correctamente.")
            return redirect("listar_estudiantes")
    else:
        formulario = EstudianteForm(instance=estudiante)

    return render(
        request,
        "estudiantes/editar_estudiantes.html",
        {"formulario": formulario, "estudiante": estudiante},
    )


@require_POST
def cambiar_estado_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.estado = not estudiante.estado
    estudiante.save(update_fields=["estado"])

    if estudiante.estado:
        messages.success(request, "El estudiante fue activado correctamente.")
    else:
        messages.success(request, "El estudiante fue desactivado correctamente.")

    return redirect("listar_estudiantes")

@require_POST
def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()

    messages.success(request, "El estudiante fue eliminado correctamente.")

    return redirect("listar_estudiantes")