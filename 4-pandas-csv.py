from os import sep
import modules._start as starter

starter.clear_console()

import pandas as pd

city_pop_file_url = "https://milliams.com/courses/data_analysis_python/city_pop.csv"

census = pd.read_csv(city_pop_file_url,
                     skiprows=5,
                     index_col='year',
                     sep=';',
                     na_values=['-1'])

# Print a row by index
print(census.loc[[2001]])

# Print a coulumn by lable
print(census['London'])

# Print a cell
print(census['London'][2001])
