# Importar la libreria 'Json'
import json

# from models import persona
# from models.persona import Persona

# Crear una variable global, como buena practica se escribe todo con mayusucla
RUTA = 'data/db.json'

# Datos globales para retornar la excepcion
DATOS_INICIALIZADOS ={
            'ultimo_id_persona': 0,
            'ultimo_id_estudiante': 0,
            'persona': [],
            'estudiante': []
        }

# Crear dos funciones
# FUNCIÓN 1: CARGAR LA DATA
def cargar():
    # EXEPCIONES:
    try:
        with open(RUTA, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        # EN CASO DE OCURRIR UNA EXCEPCION SE INICIALIZA DESDE 0
        return DATOS_INICIALIZADOS


# FUNCIÓN 2: MOSTRAR/ ALMACENAR LA DATA
def guardar(datos):
    # Open recibe 3 parametros principales: la ruta, el modo y la certificación
    with open(RUTA, 'w', encoding='utf-8') as archivo:
        # Los datos del objeto se deben guardar en al archivo, con una determinada identacion y respetando caracteres especiales
        json.dump(datos, archivo, indent=3, ensure_ascii=False)