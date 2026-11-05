from django.contrib import admin
from .models import Producto

# Register your models here.
# admin.site.register(Producto)
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'nombre',
    'precio',
    'stock',
    'descripcion'
  )

  search_Fields = ('nombre', 'descripcion', )

  ordering = ('nombre', )

  list_filter = ('precio', 'stock', )

  list_per_page = 10
