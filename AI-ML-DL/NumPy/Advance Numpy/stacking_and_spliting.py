import numpy as np

# stacking
arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])


print(np.hstack((arr_1,arr_2)))
print(np.vstack((arr_1,arr_2)))

# splitting
""" 
np.split()
equal 

np.hsplit()
np.vsplit()
"""

arr = np.array([10,20,30,40,50,60])
new_arr = np.split(arr,2)

print(new_arr)