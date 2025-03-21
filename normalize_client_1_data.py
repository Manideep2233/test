import pandas as pd
import json

# Load JSON data
with open('data/input/client_1_patients.json', 'r') as f:
    data = json.load(f) # your data here

patients = []
episodes = []
notes = []

# Iterate through episodes in JSON data
for patient in data:
    patient_info = {
        "patient_id": patient["patient_id"],
        "name": patient["name"],
        "dob": patient["dob"],
        "ssn": patient["ssn"],
        "address": patient["address"]
    }
    patients.append(patient_info)
    for episode in patient['episodes']:
        episode_info = {
            'patient_id': patient['patient_id'],
            'episode_id': episode['episode_id'],
            'admit_date_time': episode['admit_date_time'],
            'discharge_date_time': episode['discharge_date_time'],
            'admitting_diagnosis': episode['admitting_diagnosis'],
            'discharge_diagnosis': episode['discharge_diagnosis']
        }
        episodes.append(episode_info)
        for note in episode['notes']:
            note_info = {
                'note_id': note['note_id'],
                'episode_id': note['episode_id'],
                'note_date_time': note['note_date_time'],
                'text': note['text']
            }
            notes.append(note_info)

# Convert lists to DataFrames
patients_df = pd.DataFrame(patients)
episodes_df = pd.DataFrame(episodes)
notes_df = pd.DataFrame(notes)

# Write DataFrames to CSV files
patients_df.to_csv('data/output/patients.csv', index=False)
episodes_df.to_csv('data/output/episodes.csv', index=False)
notes_df.to_csv('data/output/notes.csv', index=False)
