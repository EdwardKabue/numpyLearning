import numpy as np

filedata = np.genfromtxt('data.txt', delimiter=',')
#print(filedata)
#change element data type.
filedata = filedata.astype('int32')
print(filedata)