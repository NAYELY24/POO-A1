from django.shortcuts import render
from .models import Producto

# Create your views here.
# VISTAS BASADAS EN FUNCIONES
def listar_productos(request):
    #ESTRUCTURA
        # if request.method =="POST":
        #     #EL USUARIO QUIERE ENVIAR INFORMACION AL SERVIDOR
        # else: ##request.method =="GET"
        #     #EL USUARIO QUIERE SOLICITAR INFORMACION AL SERVIDOR
    #SE REQUIERE VER TODOS LOS REGISTROS DE LA TABLA PRODUCTOS
    #SQL
    #select* from productos
    #ORM = MAPEO RELACIONAL DE OBJETOS
    # Productos con estado activo ordenados por id de forma ascendente
    productos = Producto.objects.filter(estado = True).order_by("id")

    # Se debe retornar un renderizado
    # Render = solicitud, plantilla y los datos
    return render(request, "productos/listar_productos.html", {"productos":productos})

def crear_productos(request):
    pass




