import pytest
import pandas as pd
import subprocess

from data_model import data_model


def test_patient_csv(run_submission):
    patients_df = pd.read_csv('data/output/patients.csv')
    for field in data_model['patient']:
        assert field in patients_df.columns

def test_note_csv(run_submission):
    notes_df = pd.read_csv('data/output/notes.csv')
    for field in data_model['note']:
        assert field in notes_df.columns

def test_episode_csv(run_submission):
    episodes_df = pd.read_csv('data/output/episodes.csv')
    for field in data_model['episode']:
        assert field in episodes_df.columns

