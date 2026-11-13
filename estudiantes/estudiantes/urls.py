from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_estudiantes, name="listar_estudiantes"),
    path("listar_estudiantes/", views.listar_estudiantes, name="listar_estudiantes"),
    path("crear_estudiantes/", views.crear_estudiantes, name="crear_estudiantes"),
    path("editar_estudiantes/<int:id>/", views.editar_estudiantes, name="editar_estudiantes"),
    path("cambiar_estado_estudiante/<int:id>/", views.cambiar_estado_estudiante, name="cambiar_estado_estudiante", ),
    path("eliminar_estudiante/<int:id>/", views.eliminar_estudiante, name="eliminar_estudiante"),
]