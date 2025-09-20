# np.inan(array)

import numpy as np

arr = np.array([1,2,np.nan,4,np.nan,5])


print(np.isnan(arr))


print(arr[2] == arr[0])