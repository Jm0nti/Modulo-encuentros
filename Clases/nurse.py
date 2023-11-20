import sqlite3

class Nurse:
    def __init__(self, nurse_id, name):
        self.nurse_id = nurse_id
        self.name = name

    def add_encounter(self, patient_id, date, observations):
        encounter = Encounter(patient_id, date, observations=observations)
        encounter.save_to_database()
