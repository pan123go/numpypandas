import numpy as np

print('='*30)
array = np.array([2,23,2],dtype=np.float)  #list
print(array.dtype)

#print(array)
#print('number of dimension:', array.ndim)
#print('shape:', array.shape)
#print('size:', array.size)


print('='*30)
a = np.array([[2,23,4],
			[2,32,4]])
print(a)


print('='*30)
b = np.zeros((3,4))
print(b)

print('='*30)
c = np.ones((3,4),dtype=np.int16)
print(c)

print('='*30)
d = np.empty((3,4))
print(d)

print('='*30)
e = np.arange(10,20,2)
print(e)

print('='*30)
f = np.arange(12).reshape((3,4))
print(f)

print('='*30)
g = np.linspace(1,10,10)
print(g)

print('='*30)
h = np.linspace(1,10,10).reshape(2,5)
print(h)

