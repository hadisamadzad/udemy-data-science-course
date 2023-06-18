import modules._start as starter

starter.clear_console()

from pandas import DataFrame
import pandas as pd

a = DataFrame([1, 2, 4], [4, 2, 6])
s = pd.Series([1, 2, 3, 4, 5])

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)
print(t)
print(s)

fig, ax = plt.subplots()
ax.plot(t, s)
fig.savefig('sin.png')
