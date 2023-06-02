import numpy as np

before = np.array([[1,2,3,4],[5,6,7,8]])

#print(before)

#reshape 'before' and store matrix with new shape in 'after'. Ensure the number of elements does not change.
after = before.reshape((4,2))
print(after)
after = before.reshape((2,2,2))
print(after)