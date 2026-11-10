from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # Path('nombre de la ruta', 'la vista', 'la referencia de la ruta')
    path('listar_productos/', views.primera_funcion, name="listar_productos"),
]
