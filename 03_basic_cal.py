import numpy as np

a = np.array([[10,20],
		      [30,40]])  
b = np.arange(4).reshape((2,2))

print(a,b)
c = a*b
c_dot = np.dot(a,b)
c_dot2 = a.dot(b)


a1 = np.random.random((2,4))
print(a1)
print('='*20)
print(np.sum(a1,axis=1)) #row
print(np.min(a1,axis=0)) #colume
print(np.max(a1))




#c = 10*np.sin(a)
print(c_dot2)
print(c_dot)
print(b)
print(b<3) #return bool value

#print(array)
#print('number of dimension:', array.ndim)
#print('shape:', array.shape)
#print('size:', array.size)


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

