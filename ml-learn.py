import modules._start as starter

starter.clear_console()

from pandas import Series
import numpy as np

nums = Series([15, 16, 18, 19, 22, 24, 29, 30, 34])

print(nums.median())
print(np.percentile(nums, 25))