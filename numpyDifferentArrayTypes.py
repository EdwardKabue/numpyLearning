import numpy as np

#Matrix of zeros
#print(np.zeros(5)) #1-d matrix
#print(np.zeros((2,3))) #2-d matrix
#print(np.zeros((2,3,3))) #3-d matrix

#Matrix of 1s 
#print(np.ones((4,2,2))) #3-d matrix
#print(np.ones((4,2,2), dtype="int32")) #Specify data type using 'dtype'.

#Matrix with any other number that's not 1 or 0.
# print(np.full((2,2), 99))
# print(np.full((2,2), 99, dtype='float32')) #Specify data type using 'dtype'.

#Copy existing matrix.
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
#print(np.full_like(a, 4))

#get matrix with random float numbers less than 1
#print(np.random.rand(4,2))
#print(np.random.random_sample(a.shape)) #generate matrix of random numbers with shape of existing matrix.

#generate matrix with random integers.
print(np.random.randint(7, size=(3,3)))