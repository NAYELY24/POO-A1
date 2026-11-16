
from django.urls import path
from . import views

urlpatterns = [

    path(
        'crear/',
        views.crear_producto,
        name='crear_producto'
    ),

    path(
        'listar/',
        views.listar_productos,
        name='listar_productos'
    ),

    path(
        'editar/<int:id>/',
        views.editar_producto,
        name='editar_producto'
    ),

    path(
        'desactivar/<int:id>/',
        views.desactivar_producto,
        name='desactivar_producto'
    ),

    path(
        'activar/<int:id>/',
        views.activar_producto,
        name='activar_producto'
    ),

]
