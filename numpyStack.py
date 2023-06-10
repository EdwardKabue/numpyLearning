import numpy as np

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

#sizes of the arrays to vertically stack must have the equal sizes.
#vertically stack v1 on top of v2. Generates multidimensional array with first element v1 followed by v2.
#print(np.stack([v1, v2]))

#vertically stack with copies.
#print(np.stack([v1, v2, v1, v2]))

#Horizontal stack. Adds elements from h2 rows to h1 rows.
h1 = np.ones((2,4))
h2 = np.zeros((2,2))

print( np.hstack((h1, h2)) )