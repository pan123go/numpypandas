import numpy as np

a = np.arange(4)
print(a)
b = a
c = a
d = b

b = a.copy()  #deep copy

print('a',a)
print('b',b)
print('c',c)
print('d',d)





