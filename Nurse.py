import sqlite3
from Encounter import Encounter

class Nurse:
    def __init__(self, nurse_id, name):
        self.nurse_id = nurse_id
        self.name = name

    # Llamado al metodo para crear encuentro de enfermero/a
    def add_encounter(self, patient_id, date, subjective, objective, diagnosis, observations):
        encounter = Encounter(patient_id, date, subjective, objective, diagnosis, observations)
        encounter.save_to_database()

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

    # Funcion para desplegar el menú de enfermero/a
    def nurse_menu(self):
        while True:
            print("\nMenú de Enfermera")
            print("1. Agregar encuentro")
            print("2. Ver reporte de encuentros de paciente")
            print("3. Salir")
            option = input("Seleccione una opción: ")

            if option == '1':
                patient_id = input("Ingrese el ID del paciente: ")
                date = input("Ingrese la fecha del encuentro (YYYY-MM-DD): ")
                observations = input("Ingrese las observaciones: ")
                subjective = None
                objective = None
                diagnosis = None
                self.add_encounter(patient_id, date, subjective, objective, diagnosis, observations)

            elif option == '2':
                buscar_id = int(input("Ingrese el ID del paciente: "))
                self.user_reports(buscar_id)

            elif option == '3':
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")