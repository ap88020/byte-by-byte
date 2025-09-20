import numpy as np

arr = np.array([1.3,2.4,3.5,4.6])

print(arr)
print(arr.dtype)

arr_int = arr.astype(int)
print(arr_int)
print(arr_int.dtype)