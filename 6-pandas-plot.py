from pandas.core.series import Series
import modules._start as starter

starter.clear_console()

import pandas as pd
import matplotlib.pyplot as plt

city_pop_file_url = "https://milliams.com/courses/data_analysis_python/rain.csv"

df = pd.read_csv(
    city_pop_file_url,
    # skiprows=5,
    # index_col='year',
    # sep=';',
    # na_values=['-1'])
)
#print(df['Oxford'])

years = Series(df.index, index=df.index).apply(str)
decades = years.apply(lambda x: x[:3] + '0')

df['Decade'] = decades

by_decade = df.groupby("Decade").mean()

plot = by_decade['Oxford'].plot.bar()
plot.set_ylabel("Temperature ($^\circ$F)")

fig = plot.get_figure()
fig.savefig("oxford-temperature")

print('Figure saved!')