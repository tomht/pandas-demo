import pandas as pd

complaints = pd.read_csv('data/311-service-requests.csv')

print(complaints['Complaint Type'])

print(complaints[:5])

print(complaints['Complaint Type'][:5])

print(complaints[['Complaint Type', 'Borough']][:10])

print(complaints['Complaint Type'].value_counts())

print(complaints['Complaint Type'].value_counts())[:10]
