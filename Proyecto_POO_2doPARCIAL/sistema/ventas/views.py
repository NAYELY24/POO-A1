from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed

from .models import Producto
from .forms import ProductoForm


# CREAR PRODUCTO
def crear_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_productos')
    else:
        formulario = ProductoForm()
    return render(
        request,
        'crear_producto.html',
        {'formulario': formulario}
    )


# LISTAR PRODUCTOS
def listar_productos(request):
    productos = Producto.objects.all().order_by('id')
    return render(
        request,
        'listar_productos.html',
        {'productos': productos}
    )


# EDITAR PRODUCTO
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        formulario = ProductoForm(
            request.POST,
            instance=producto
        )
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_productos')
    else:
        formulario = ProductoForm(instance=producto)

    return render(
        request,
        'editar_producto.html',
        {'formulario': formulario}
    )


# DESACTIVAR PRODUCTO
def desactivar_producto(request, id):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    producto = get_object_or_404(Producto, id=id)
    producto.estado = False
    producto.save()

    return redirect('listar_productos')


# ACTIVAR PRODUCTO
def activar_producto(request, id):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    producto = get_object_or_404(Producto, id=id)
    producto.estado = True
    producto.save()

    return redirect('listar_productos')


# ELIMINAR PRODUCTO
def eliminar_producto(request, id):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    producto = get_object_or_404(Producto, id=id)
    producto.delete()

    return redirect('listar_productos')
