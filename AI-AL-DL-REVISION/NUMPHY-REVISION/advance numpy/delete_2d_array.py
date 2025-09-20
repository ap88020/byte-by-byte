import numpy as np

arr_2d = np.array([[10,20,30],[40,50,60]])

new_2d_arr = np.delete(arr_2d,0,axis=0)

print(new_2d_arr)