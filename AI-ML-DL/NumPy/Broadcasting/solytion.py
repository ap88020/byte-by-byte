import numpy as np

prices = np.array([100,200,300])

discount = 10

final_price = prices - (prices * 10/100)

print(final_price)