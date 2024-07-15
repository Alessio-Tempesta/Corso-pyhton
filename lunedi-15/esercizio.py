import numpy as np

arr = np.array([1, 2, 3, 4 ,5])

arr2d = np.array([[1, 2, 3], [4, 5, 6 ]])

sum_arr = np.sum(arr)
print("lo somma degli elemenyi di arr:",sum_arr)

# np.ones()
arr_ones = np.ones(5)
print("Array 1d : ", arr_ones)

# np.arange()
arr = np.arange(10)
print(arr)

# reshape()
arr = np.arange(6)
resahped_arr = arr.reshape((2, 3))
print(resahped_arr)