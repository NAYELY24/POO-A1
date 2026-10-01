#ENUNCIADO
##SE DEBE CREAR 2 CLASES UNA CLASE PERSONA Y UNA CLASE ESTUDIANTE (ESTUDIANTE HEREDA DE PERSONA)
#POR CADA CLASE DEBE CREAR UN CRUD (CREAR - LEER - ACTUALIZAR - ELIMINAR), GUARDAR TODA LA INFORMACION (LOS OBJETOS CREADOS) EN UN ARCHIVO .json PARA MANTENER LA
# PERSISTENCIA DE LA DATA. GENERAR IDENTIFICADORES AUTOMATICOS Y VALIDAR DATOS

from services import persona_service
from services import estudiante_service

def menu():
    while True:
        print('----Menú del proyecto----')
        print('1. Crear persona')
        print('2. Listar persona')
        print('3. Salir')

        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            nombre = input('Ingrese el nombre de la persona')
            edad = int(input('Ingrese la edad de la persona'))
            persona_service.crear(nombre, edad)
            print('Persona creada correctamente')

        elif opcion == 2:
            pass

        elif opcion == 3:
            return

menu()