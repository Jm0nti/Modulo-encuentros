import sqlite3
from Encounter import Encounter

class Doctor:
    def __init__(self, doctor_id, name):
        self.doctor_id = doctor_id
        self.name = name

    # Llamado al metodo para crear encuentro de medico
    def add_encounter(self, patient_id, date, subjective, objective, diagnosis, observations):
        encounter = Encounter(patient_id, date, subjective, objective, diagnosis, observations)
        encounter.save_to_database()
    
    # Funcion para añadir nota aclaratoria a un encuentro especifico cerrado anteriormente
    def add_clarify(self, buscar_id):
        conn = sqlite3.connect('BDs/encuentros.db')
        cursor = conn.cursor()

        nota_aclaratoria = input("Ingrese la nota aclaratoria: ")
        cursor.execute('UPDATE Encuentros SET Nota_aclaratoria = ? WHERE ID = ?', (nota_aclaratoria, buscar_id))
        conn.commit()
        conn.close()

    # Funcion para acceder al reporte de todos los encuentros de un paciente
    def user_reports(self, buscar_id):
        conn = sqlite3.connect('BDs/encuentros.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Encuentros WHERE Patient_id = ?', (buscar_id,))
        encounters = cursor.fetchall()

        # Mostrar la información de los encuentros encontrados
        for idx, enc in enumerate(encounters, start=1):
            print("\n")
            print(f"Encuentro {idx}:")
            print(f"Subjetivo: {enc[3]}")
            print(f"Objetivo: {enc[4]}")
            print(f"Diagnóstico: {enc[5]}")
            print(f"Observaciones: {enc[6]}")
            print(f"Notas aclaratorias: {enc[7]}")
        
        conn.commit()
        conn.close()

    # Funcion para desplegar el menú de medico
    def doctor_menu(self):
        while True:
            print("\nMenú de Médico")
            print("1. Agregar encuentro")
            print("2. Ver reporte de encuentros de paciente")
            print("3. Añadir nota aclaratoria a un encuentro creado")
            print("4. Salir")
            option = input("Seleccione una opción: ")

            # Funcion para Agregar un encuentro
            if option == '1':
                patient_id = int(input("Ingrese el ID del paciente: "))
                date = input("Ingrese la fecha del encuentro (YYYY-MM-DD): ")
                subjective = input("Ingrese la información subjetiva: ")
                objective = input("Ingrese la información objetiva: ")
                diagnosis = input("Ingrese el diagnóstico: ")
                observations = input("Ingrese las observaciones: ")

                self.add_encounter(patient_id, date, subjective, objective, diagnosis, observations)

            # Funcion para visualizar reporte de encuentros de un paciente
            elif option == '2':
                buscar_id = int(input("Ingrese el ID del paciente: "))
                self.user_reports(buscar_id)

            elif option == '3':
                buscar_id = int(input("Ingrese el ID del encuentro: "))
                self.add_clarify(buscar_id)

            elif option == '4':
                break

            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")