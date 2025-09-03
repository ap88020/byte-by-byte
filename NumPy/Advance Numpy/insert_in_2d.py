import numpy as np

arr_2d = np.array([[10,20,30],[40,50,60]])
# print(arr_2d)

# new_arr = np.insert(arr_2d, 2, [70,80,90], axis=1)
# print(new_arr)

new_arr = np.insert(arr_2d, 2, [100,000 ,300], axis=0)
print(new_arr)
