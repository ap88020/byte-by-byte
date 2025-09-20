import numpy as np

arr = np.array([1,2,np.inf , 3, -np.inf])

print(np.isfinite(arr))