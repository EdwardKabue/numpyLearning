import numpy as np

stats = np.array([[1,2,3],[4,5,6]])

#get smallest value in the matrix
#print(np.min(stats))

#get largest value in the matrix
#print(np.max(stats))

#get the minimum value for each row in the matrix
#print(np.min(stats, axis=1))

#get the minimum value for each column in the matrix
#print(np.min(stats, axis=0))

#get the maximum value for each row in the matrix
#print(np.max(stats, axis=1))

#get the maximum value for each column in the matrix
#print(np.max(stats, axis=0))

#sum up all the elements in the matrix.
#print(np.sum(stats))

#sum up all the elements in each column the matrix.
print(np.sum(stats, axis=0))