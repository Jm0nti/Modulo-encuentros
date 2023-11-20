import sqlite3

class Doctor:
    def __init__(self, doctor_id, name):
        self.doctor_id = doctor_id
        self.name = name

    def add_encounter(self, patient_id, date, subjective, objective, diagnosis, observations):
        encounter = Encounter(patient_id, date, subjective, objective, diagnosis, observations)
        encounter.save_to_database()
