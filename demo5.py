import pandas as pd

requests = pd.read_csv('data/311-service-requests.csv')

print(requests['Incident Zip'].unique())

# How can we ensure "null" data is recognised? And how can we make sure zip codes are treated as strings?

na_values = ['NO CLUE', 'N/A', '0', '00000']
requests = pd.read_csv('data/311-service-requests.csv', na_values=na_values, dtype={'Incident Zip': str})

print(requests['Incident Zip'].unique())

# How can we trim multi-part zip codes?

requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)

print(requests['Incident Zip'].unique())