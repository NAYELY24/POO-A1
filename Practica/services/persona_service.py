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
    datos['personas'].append(persona)
    # Aqui se guardan los datos actualizados en el archivo JSON
    repo_json.guardar(datos)
    return datos['ultimo_id_persona']

def leer():
    datos = repo_json.cargar()
    return datos['personas']

def actualizar(id_persona, nombre, edad):
    datos = repo_json.cargar()
    if datos['personas']:
        for persona in datos['personas']:
            if persona['id_persona'] == id_persona:
                persona['nombre'] = nombre
                persona['edad'] = edad
                repo_json.guardar(datos)
                return True
            else:
                return False
    else:
        raise ValueError('No existen personas registradas')


def eliminar(id_persona):
    datos = repo_json.cargar()  # Viene todos las llaves del  diccionario en REPO_JSON
    # Para verificar que datos posee valores/elementos
    if datos['personas']:
        for persona in datos['personas']:
            if persona['id_persona'] == id_persona:
                datos['personas'].remove(persona)
                repo_json.guardar(datos)
                return True
            else:
                return False
    else:
        raise ValueError('No existen personas registradas')

def buscar_por_cedula():
    pass

def filtrar_por_fecha():
    pass

def filtrar_por_estado():
    pass

