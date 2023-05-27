import numpy as np

#initialise numpy array
a = np.array([1,2,3], dtype='int32')
#print(a)

#initialise 2d array of float values
b = np.array([[9.0,8.9,7.7],[8.9,6.7,5.9]])
#print(b)

#get number of array dimensions
#print(b.ndim)

#get shape of array. I.e. (rows, columns).
#print(b.shape)

#get array data type
print(a.dtype)

#get size of the array items in bytes
print(a.itemsize)

#get the total number of items in the array.
print(b.size)