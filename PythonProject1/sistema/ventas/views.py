from django.shortcuts import render
from .models import Producto

# Create your views here.
# VISTAS BASADAS EN FUNCIONES
def primera_funcion(request):
    #ESTRUCTURA
        # if request.method =="POST":
        #     #EL USUARIO QUIERE ENVIAR INFORMACION AL SERVIDOR
        # else: ##request.method =="GET"
        #     #EL USUARIO QUIERE SOLICITAR INFORMACION AL SERVIDOR
    #SE REQUIERE VER TODOS LOS REGISTROS DE LA TABLA PRODUCTOS
    #SQL
    #select* from productos
    #ORM = MAPEO RELACIONAL DE OBJETOS
    productos = Producto.objects.all()




