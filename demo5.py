import pandas as pd

requests = pd.read_csv('data/311-service-requests.csv')

print(requests['Incident Zip'].unique())

na_values = ['NO CLUE', 'N/A', '0', '00000']
requests = pd.read_csv('data/311-service-requests.csv', na_values=na_values, dtype={'Incident Zip': str})

print(requests['Incident Zip'].unique())

requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)

print(requests['Incident Zip'].unique())