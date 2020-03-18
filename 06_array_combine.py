import numpy as np

A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
#C = np.vstack((A,B))
#D = np.hstack((A,B))
#print(A.shape,C.shape)
#print(np.vstack((A,B))) #vertical stack
#
#print(C,D)
#print(A)
#print(A.T)#can not transpose
#print(A[np.newaxis,:])

C = np.concatenate((A,B),axis=1)
print(C)
