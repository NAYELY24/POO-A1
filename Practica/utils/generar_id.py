# Generar funciones para crear ID para Persona y Estudiante
def generar_id_persona(datos):
    datos = datos['ultimo_id_persona']  ## 0
    # Variable para que el ID vaya aumentando de 1 en 1
    datos += 1
    return datos

def generar_id_estudiante(datos):
    datos = datos['ultimo_id_estudiante']  ## 0
    # Variable para que el ID vaya aumentando de 1 en 1
    datos += 1
    return datos