import modules._start as starter

starter.clear_console()

import numpy as np
from pandas import DataFrame

axs = np.arange(100)
b = np.arange(100) * 2

df = DataFrame({'a': axs, 'b': b})
print(df.corr())

# Housing
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

housing_data = fetch_california_housing()
housing = DataFrame(housing_data.data, columns=housing_data.feature_names)
corr = housing.corr()

print(corr)

#print(corr['MedInc']['AveRooms'])

import seaborn as sns

cmap = sns.diverging_palette(30, 200, as_cmap=True)
heat = sns.heatmap(corr, cmap=cmap)

fig = heat.get_figure()
fig.savefig("correlation-heatmap")

from pandas.plotting import scatter_matrix

axs = scatter_matrix(housing, figsize=(24, 24))
print(axs)
axs[0, 0].get_figure().savefig("scatter-matrix")
