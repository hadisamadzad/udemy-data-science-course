import modules._start as starter

starter.clear_console()

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

# Reading data
city_pop_file_url = "https://milliams.com/courses/applied_data_analysis/linear.csv"
data = pd.read_csv(city_pop_file_url)

# Model
model = LinearRegression(fit_intercept=True)
model.fit(data[['x']], data['y'])

# Results
print(model.coef_[0])
print(model.intercept_)

# Prediction
x_fit = DataFrame([data['x'].min(), data['x'].max()])
y_pred = model.predict(x_fit)

# Visualization
plot = data.plot.scatter('x', 'y')
plot.plot(x_fit[0], y_pred, c='green', linestyle=":")

plot.get_figure().savefig("x-y-scatter-predicted")

# Other
print(data.ndim)
print(data.shape)