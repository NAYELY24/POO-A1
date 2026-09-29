# En los servicios se coloca toda la logica de mensaje(Finalizar un CRUD):
from repository import repo_json

def listar():
    # En la variable datos se almacena TODOS los registros
    datos = repo_json.cargar()
    # De todos los dato filtra aquellos que pertenecen a la lista de personas
    return datos['personas']

def crear():
    pass

def actualizar():
    pass

def eliminar():
    pass

def buscar_por_cedula():
    pass

def filtrar_por_fecha():
    pass

def filtrar_por_estado():
    pass

