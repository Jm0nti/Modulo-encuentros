import sqlite3

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
