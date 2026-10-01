# En los servicios se coloca toda la logica de mensaje (Finalizar un CRUD):
from repository import repo_json
from utils.generar_id import generar_id_persona

def listar():
    # En la variable datos se almacena TODOS los registros
    datos = repo_json.cargar()
    # De todos los dato filtra aquellos que pertenecen a la lista de personas
    return datos['personas']

def crear(nombre, edad):
    # Cuando se crea un registro se requiere que el ID de la persona empiece desde 1 y se vaya incrementando de 1 en 1.
    # Paso1: Abrir el archivo JSON para verificar el ultimo ID de una persona
    datos = repo_json.cargar()
    generar_id_persona(datos)
    id_persona = generar_id_persona(datos)

    persona= {'id_persona': id_persona, 'nombre': nombre, 'edad': edad}
    # Agregar en un lista los registros de una persona en la memoria
    datos['persona'].append(persona)
    # Aqui se guardan los datos actualizados en el archivo JSON
    repo_json.guardar(datos)
    return datos['ultimo_id_persona']


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
