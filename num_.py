#NumPy (Numerical Python) is a fundamental library for numerical operations in Python. 
/*
Benefits of using NumPy over standard Python lists:
NumPy arrays are more compact in memory and faster in execution.
NumPy provides a wide range of mathematical functions and operations optimized for scientific computing.
*/

#NumPy arrays are the core data structure in NumPy. They are similar to Python lists but more efficient and optimized for numerical operations.

import numpy as np
# Creating a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# Creating a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)
print("Shape of arr1:", arr1.shape)
print("Shape of arr2:", arr2.shape)
print("Number of dimensions in arr2:", arr2.ndim)
print("Size of arr2 (total number of elements):", arr2.size)
print("Data type of elements in arr1:", arr1.dtype)
