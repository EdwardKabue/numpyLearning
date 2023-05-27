import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

#get a specific element using format arrayVariableName[row, column]
#print(a[1,5])

#get a specific element using negative notation format. I.e. arrayVariableName[row, -column]. Column is negativley offset from the last item.
#print(a[1,-2])

#get a specific row. E,g. get first row.
#print(a[0, :])

#get a specific column. E,g. get second column.
#print(a[:, 2])

#get row elements by skipping desired number of elements. E.g. get row elements from 1st row by skipping 2 elements starting at element 2 and ending with element 7 exclusive.
#print(a[0, 1:6:2])
#negative notation also works. I.e. Column is negativley offset from the last item.
#print(a[0, 1:-1:2])

#modify an element
a[1,5] = 20
# print(a)

#modify a column
a[:, 2] = 5 #same value for the whole column
a[:, 3] = [1, 2] #different values on different rows.
#print(a)

#3-d example
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

#get specific element from 3-d array
print(b[0,1,1])