import pandas as pd
import matplotlib.pyplot as plt

# Easily read a CSV with one line of code.

# Various options are supported: different separating characters, encodings, etc.

# Choose a column to be the index of the data.

df = pd.read_csv('data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')

# Select rows or columns.

print(df[:3])

print(df['Berri 1'])

# Easily plot the data.

df['Berri 1'].plot()
plt.show()
