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
#print(np.random.randint(7, size=(3,3)))

#generate identity matrix
#print(np.identity(4))

#repeat an array.
arr = np.array([[1,2,3]])
r1 = np.repeat(arr, 3, axis=0)
#print(r1)

#modify array using other arrays.
output = np.ones((5,5))
#print(output)
z = np.zeros((3,3))
#print(z)
z[1,1] = 9
#print(z)

output[1:4,1:4] = z
#print(output)

#make copy of existing array
b = np.array([1,2,3])
c = b #c and b point to the same array. Therefore, any change in c will reflect in the b reference.
#print(c)
c = b.copy() #make a copy of the array in b which is a new array unique to c.
c[0] = 100
#print(c)
