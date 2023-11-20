import sqlite3
from Doctor import Doctor
from nurse import Nurse
from patient import Patient
from Encounter import Encounter


# Función para autenticar médico o enfermera
def authenticate_user(user_type):
    conn = sqlite3.connect(f'{user_type}.db')
    cursor = conn.cursor()

    name = input("Ingrese su nombre: ")
    password = input("Ingrese su contraseña: ")

    cursor.execute('SELECT * FROM Lista_{}s WHERE name=? AND password=?'.format(user_type.capitalize()), (name, password))
    user = cursor.fetchone()

    conn.close()
    return user

# Función para menú de enfermera
def nurse_menu():
    while True:
        print("\nMenú de Enfermera")
        print("1. Agregar encuentro")
        print("2. Salir")
        option = input("Seleccione una opción: ")

        if option == '1':
            add_encounter('nurse')
        elif option == '2':
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Función para menú de médico
def doctor_menu():
    while True:
        print("\nMenú de Médico")
        print("1. Agregar encuentro")
        print("2. Salir")
        option = input("Seleccione una opción: ")

        if option == '1':
            add_encounter('doctor')
        elif option == '2':
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Función para agregar encuentro
def add_encounter(user_type):
    patient_id = int(input("Ingrese el ID del paciente: "))
    date = input("Ingrese la fecha del encuentro (YYYY-MM-DD): ")
    observations = input("Ingrese las observaciones: ")

    conn = sqlite3.connect('encuentros.db')
    cursor = conn.cursor()

    if user_type == 'Medico':
        subjective = input("Ingrese la información subjetiva: ")
        objective = input("Ingrese la información objetiva: ")
        diagnosis = input("Ingrese el diagnóstico: ")

        cursor.execute('INSERT INTO Encuentros (ID, fecha, Subjetivo, Objetivo, diagnostico, observaciones) VALUES (?, ?, ?, ?, ?, ?)',
                       (patient_id, date, subjective, objective, diagnosis, observations))
    elif user_type == 'Enfermero':
        cursor.execute('INSERT INTO Encuentros (ID, fecha, observaciones) VALUES (?, ?, ?)',
                       (patient_id, date, observations))

    conn.commit()
    conn.close()

# Inicio de sesión
def start_program():
    print("Bienvenido al sistema de la clínica.")
    while True:
        print("Por favor, seleccione el tipo de usuario:")
        print("1. Médico")
        print("2. Enfermera")
        print("3. Salir")
        user_type_option = input("Seleccione una opción: ")

        if user_type_option == '1':
            user_type = 'Medico'
        elif user_type_option == '2':
            user_type = 'Enfermero'
        elif user_type_option == '3':
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

        if user_type in ['Medico', 'Enfermero']:
            user = authenticate_user(user_type)
            if user:
                if user_type == 'Medico':
                    doctor_menu()
                else:
                    nurse_menu()
            else:
                print("Credenciales incorrectas. Por favor, inténtelo de nuevo.")

start_program()
