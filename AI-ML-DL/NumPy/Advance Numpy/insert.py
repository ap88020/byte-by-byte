""" 
np.insert(array,index,value,axios=None)

array -> original array,
index -
value -
axios = 0 -> row , 1 -> col
"""

import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr)

new_arr = np.insert(arr,2,100)
print(new_arr)

