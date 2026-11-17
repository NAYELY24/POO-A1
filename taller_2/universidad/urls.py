from django.urls import path
from . import views

urlpatterns = [
    path('personas/', views.listar_persona, name='listar_persona'),
]
