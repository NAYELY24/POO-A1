"""
URL configuration for sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from ventas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listar_productos, name='inicio'),  # <-- ESTA ES LA QUE TE FALTA
    path('crear/', views.crear_producto, name='crear_producto'),
    path('listar/', views.listar_productos, name='listar_productos'),
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('desactivar/<int:id>/', views.desactivar_producto, name='desactivar_producto'),
    path('activar/<int:id>/', views.activar_producto, name='activar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]







