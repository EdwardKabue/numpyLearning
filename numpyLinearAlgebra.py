import numpy as np

a = np.ones((2,3))
# print(a)

b = np.full((3,2), 2)
# print(b)

#multiply 2 matrices
#print(np.matmul(a,b))

c = np.identity(3)
#get determinant of a matrix
print(np.linalg.det(c))