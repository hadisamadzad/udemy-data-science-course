import modules._start as starter

starter.clear_console()

from pandas import DataFrame

df = DataFrame({"year": [2001, 2002, 2003, 2004], "age": [11, 12, 13, 14]})

#print(df)

print(df.idxmax())
