import numpy as np

arr = np.array([1,2,np.nan , 5, np.nan])

resut = np.nan_to_num(arr,nan=100)

print(resut)