import pandas as pd
import matplotlib.pyplot as plt

complaints = pd.read_csv('data/311-service-requests.csv')

# Combine selection of rows and columns.

print(complaints['Complaint Type'][:5])

# Select more than one column.

print(complaints[['Complaint Type', 'Borough']][:10])

# What are the top 10 most common complaints?

complaint_counts = complaints['Complaint Type'].value_counts()
print(complaint_counts)

complaint_counts[:10].plot(kind='bar')
plt.show()
