#ENUNCIADO
##SE DEBE CREAR 2 CLASES UNA CLASE PERSONA Y UNA CLASE ESTUDIANTE (ESTUDIANTE HEREDA DE PERSONA)
#POR CADA CLASE DEBE CREAR UN CRUD (CREAR - LEER - ACTUALIZAR - ELIMINAR), GUARDAR TODA LA INFORMACION (LOS OBJETOS CREADOS) EN UN ARCHIVO .json PARA MANTENER LA
# PERSISTENCIA DE LA DATA. GENERAR IDENTIFICADORES AUTOMATICOS Y VALIDAR DATOS

from services import persona_service
from services import estudiante_service
from models.persona import Persona

def menu():
    while True:
        print('----Menú del proyecto----')
        print('1. Crear persona')
        print('2. Listar persona')
        print('3. Actualizar persona')
        print('4. Eliminar persona')
        print('5. Buscar persona')
        print('6. Llamar al metodo presentarse')
        print('7. Salir')

        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            nombre = input('Ingrese el nombre de la persona')
            edad = int(input('Ingrese la edad de la persona'))
            persona_service.crear(nombre, edad)
            print('Persona creada correctamente')

        elif opcion == '2':
            print(persona_service.listar())

        elif opcion == '3':
            id_persona = int(input('Ingrese el id de la persona: '))
            nombre = input('Ingrese el nombre de la persona: ')
            edad = int(input('Ingrese la edad de la persona'))
            actualizar = persona_service.actualizar(id_persona, nombre, edad)
            if actualizar:
                print('La persona se actualizo correctamente...')
            else:
                print('El ID ingresado no existe')


        elif opcion == '4':
            id_persona = int(input('Ingrese el id de la persona: '))
            eliminacion_exitosa = persona_service.eliminar(id_persona)
            if eliminacion_exitosa:
                print('Persona eliminada correctamente')
            else:
                print('El ID ingresado no existe')

        elif opcion == '5':
            id_persona = int(input('Ingrese el ID de la persona que quiere buscar: '))
            print(persona_service.buscar_por_id(id_persona))

        elif opcion == '6':
            # REALIZARLO EN UNA FUNCION CREADA EN SERVICE
            id_persona = int(input('Ingrese el ID del registro: '))
            persona = persona_service.buscar_por_id(id_persona)
            p1 = Persona(persona['id_persona'], persona['nombre'], persona['edad'])
            print(p1.presentarse())

        elif opcion == '7':
            return
menu()

def menu2():
    while True:
        print('----Menú del proyecto----')
        print('1. Crear estudiante')
        print('2. Listar estudiante')
        print('3. Salir')

        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            curso = input('Ingrese el curso del estudiante: ')
            estudiante_service.crear(curso)
            print('Estudiante creado correctamente')

        elif opcion == 2:
            pass

        elif opcion == 3:
            return

# menu2()
