import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')

print(df[:3])

print(df['Berri 1'])

df['Berri 1'].plot()
plt.show()
