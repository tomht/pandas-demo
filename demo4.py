import pandas as pd

bikes = pd.read_csv('data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')

berri_bikes = bikes[['Berri 1']]

# Do people bike more on weekends or on weekdays?

print(berri_bikes.index)

print(berri_bikes.index.weekday)

berri_bikes['weekday'] = berri_bikes.index.weekday

weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(weekday_counts)