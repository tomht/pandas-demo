import pandas as pd

complaints = pd.read_csv('data/311-service-requests.csv')

noise_complaints = complaints[complaints['Complaint Type'] == "Noise - Street/Sidewalk"]

print(noise_complaints[:3])

print(noise_complaints[:3][['Complaint Type', 'Borough', 'Created Date', 'Descriptor']])

# Which borough has made the most noise complaints?
print(noise_complaints['Borough'].value_counts())