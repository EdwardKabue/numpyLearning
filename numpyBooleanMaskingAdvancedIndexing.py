import numpy as np

filedata = np.genfromtxt('data.txt', delimiter=',')
#print(filedata)
#change element data type.
filedata = filedata.astype('int32')

#get boolean value for each element based on a condition. E.g. test if element is greater than 50.
#print(filedata > 50)

#get values based on condition filter.
#print(filedata[filedata > 50])

a = np.array([1,2,3,4,5,6,7,8,9])

#get items based on a list of indexes.
#print(a[[2,3,8]])

#test if condition is met for any value along columns of array and return boolean
#print(np.any(filedata > 50, axis=0))

#test if condition is met for all values along columns of array and return boolean
#print(np.all(filedata > 50, axis=0))

#test if condition is met for any value along rows of array and return boolean.
#print(np.any(filedata > 50, axis=1))

#test if condition is met for all values along rows of array and return boolean
#print(np.all(filedata > 50, axis=1))

#get boolean value for each element based on multiple conditions.
#print( ((filedata > 50) & (filedata < 100)) )

#get boolean value for each element based on negation of multiple conditions.
print( ~((filedata > 50) & (filedata < 100)) )