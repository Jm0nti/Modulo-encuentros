import sqlite3

class Doctor:
    def __init__(self, doctor_id, name):
        self.doctor_id = doctor_id
        self.name = name

    def add_encounter(self, patient_id, date, subjective, objective, diagnosis, observations):
        encounter = Encounter(patient_id, date, subjective, objective, diagnosis, observations)
        encounter.save_to_database()

class Nurse:
    def __init__(self, nurse_id, name):
        self.nurse_id = nurse_id
        self.name = name

    def add_encounter(self, patient_id, date, observations):
        encounter = Encounter(patient_id, date, observations=observations)
        encounter.save_to_database()

class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

class Encounter:
    def __init__(self, patient_id, date, subjective=None, objective=None, diagnosis=None, observations=None):
        self.patient_id = patient_id
        self.date = date
        self.subjective = subjective
        self.objective = objective
        self.diagnosis = diagnosis
        self.observations = observations

    def save_to_database(self):
        conn = sqlite3.connect('encuentros.db')
        cursor = conn.cursor()

        if self.subjective is not None:
            cursor.execute('INSERT INTO Encuentros (ID_paciente, fecha, Subjetivo, Objetivo, diagnostico, observaciones) VALUES (?, ?, ?, ?, ?, ?)',
                           (self.patient_id, self.date, self.subjective, self.objective, self.diagnosis, self.observations))
        else:
            cursor.execute('INSERT INTO Encuentros (ID_paciente, fecha, observaciones) VALUES (?, ?, ?)',
                           (self.patient_id, self.date, self.observations))

        conn.commit()
        conn.close()
