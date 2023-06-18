import modules._start as starter

starter.clear_console()

from pandas import Series

s = Series([5, -12, 4, 2, 5, 6], index=[2, 2, 3, 4, 5, 6])
result = s > 5
print(s.values)
print(s)
print(result)