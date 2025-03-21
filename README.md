## Data Engineer take home challenge

This challenge provides working code that parses one client's data. Your task is to modify or create new code that will handle a new client's data.

You will first need to install the required dependencies using the included conda `env` file:  
`conda env create -f env.yaml`

Alternatively, there is a `requirements.txt` file if you prefer to use `venv`.

You should now be able to run `normalize_client_1_data.py`. Check that this will run without errors. And run `pytest test_normalization.py`.

### Challenge

The `normalize_client_1_data.py` script parses data in `data/client_1_patients.json`, normalizes into 3 tables (well, dataframes), and then writes them to CSVs (`episodes`, `notes`, and `patients`). 

The data model for output data is as follows:

```python
{'notes': ['note_id', 'episode_id', 'note_date_time', 'text'],
 'episodes': ['episode_id', 'patient_id', 'admit_date_time', 'discharge_date_time', 'admitting_diagnosis', 'discharge_diagnosis'],
 'patients': ['patient_id', 'name', 'dob', 'ssn', 'address']}
```

Client 1's data has the following structure:

* patient
  - episodes
  - notes

For Client 1, the field names within patient, episode and notes happen to be the same as the field names in the data model.

Your task is to finish the script `normalize_client_data.py` so that it that will parse data from `data/client_1_patients.json` and `data/client_2_episodess.json`, normalize it to the same 3 tables, and then write them to the same CSVs.

As you might guess from the file names, the data structure for clients 1 and 2 differ. Client 2's data also has a different field names than the data model. All fields in the data model _do_ have an equivalent field in client 2 data, however.

For your convenience, the `data` directory also contains an example record for each client data file (`client_1_patients_example.json` and `client_2_episodes_example.json`).

### Evaluation Criteria

There are many ways to solve the challenge. An ideal solution:
* works on both client data files and writes them to the same CSVs following the data model
* does not create inaccurate or duplicate data
* could be easily modified to handle additional clients
* contains clean code that is easy to read and understand
* easily changed from a script to a module

Basic tests are included in `test_normalization.py`. Hidden tests will also be run after submission to check the criteria above.

## Submitting your solution
Please push your changes to the `main` branch of this repository. You can push one or more commits.

Once you are finished with the task, please click the Submit Solution link on [this screen](https://app.codescreen.com/candidate/0c7617d5-c743-454b-b3e3-1c0b9ffdba28].).

### Good luck!
## License

At CodeScreen, we strongly value the integrity and privacy of our assessments. As a result, this repository is under exclusive copyright, which means you **do not** have permission to share your solution to this test publicly (i.e., inside a public GitHub/GitLab repo, on Reddit, etc.). <br>

## Submitting your solution

Please push your changes to the `main branch` of this repository. You can push one or more commits. <br>

Once you are finished with the task, please click the `Submit Solution` link on <a href="https://app.codescreen.com/candidate/18a7474a-2232-437a-b484-d4fd4a07e9bf" target="_blank">this screen</a>.