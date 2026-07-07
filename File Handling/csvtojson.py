import pandas as pd

# Load CSV and export to standard JSON format array
pd.read_csv('acs.csv').to_json('output.json', orient='records', indent=4)
