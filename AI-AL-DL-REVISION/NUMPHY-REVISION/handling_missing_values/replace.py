import numpy as np

arr = np.array([1,2,np.inf,5,-np.inf,6])

print(arr)

print(np.nan_to_num(arr,posinf=100,neginf=-  100))

