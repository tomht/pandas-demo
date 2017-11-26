import pandas as pd

bikes = pd.read_csv('data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')

berri_bikes = bikes[['Berri 1']]

# Do people bike more on weekends or on weekdays?

# The index is the date of the bike ride. We can extract the weekday from that.

print(berri_bikes.index)

print(berri_bikes.index.weekday)

# We can set the weekday as an additional column in the data.

berri_bikes['weekday'] = berri_bikes.index.weekday

# Then we can do some aggregation on the weekday column.

weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)

# Replace the index for readability.

weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(weekday_counts)