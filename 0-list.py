import os

clear = lambda: os.system('clear')
clear()

a = ['a', 'Hadi', 3]
a.insert(3, 22)

for i, item in enumerate(a):
    print(f"{i} is {item}")
    print(isinstance(item, str))
