import numpy as np

A = np.arange(14,2,-1).reshape((3,4))

print(A)
print(np.argmin(A))
print(np.argmax(A))
print(np.mean(A))
print(A.mean())
print(np.mean(A,axis=0))
print(np.average(A))
print(np.median(A))
print(np.cumsum(A))
print(np.diff(A))
print(np.nonzero(A))
print(np.sort(A))
print(np.transpose(A))
print((A.T))
print((A.T).dot(A))

print(np.clip(A,5,9))





















#print('='*30)
#a = np.array([[2,23,4],
#			[2,32,4]])
#print(a)
#
#
#print('='*30)
#b = np.zeros((3,4))
#print(b)
#
#print('='*30)
#c = np.ones((3,4),dtype=np.int16)
#print(c)
#
#print('='*30)
#d = np.empty((3,4))
#print(d)
#
#print('='*30)
#e = np.arange(10,20,2)
#print(e)
#
#print('='*30)
#f = np.arange(12).reshape((3,4))
#print(f)
#
#print('='*30)
#g = np.linspace(1,10,10)
#print(g)
#
#print('='*30)
#h = np.linspace(1,10,10).reshape(2,5)
#print(h)

