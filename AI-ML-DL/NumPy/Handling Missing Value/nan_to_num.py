import numpy as np

arr = np.array([1,2,np.nan,3,np.nan,4])

print(arr)
# print(np.isnan(arr))

cleaned_arr = np.nan_to_num(arr)
print(cleaned_arr)