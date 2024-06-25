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


#Example
import numpy as np

# Array creation
arr = np.array([1, 2, 3, 4, 5])
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
range_arr = np.arange(0, 10, 2)

print("Array:", arr)
print("Array of zeros:\n", zeros)
print("Array of ones:\n", ones)
print("Array with a range of values:", range_arr)

# Basic operations
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

addition = arr1 + arr2
subtraction = arr2 - arr1
multiplication = arr1 * 2
division = arr2 / 10

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# Statistical functions
sum_arr = np.sum(arr)
mean_arr = np.mean(arr)
median_arr = np.median(arr)
std_arr = np.std(arr)

print("Sum:", sum_arr)
print("Mean:", mean_arr)
print("Median:", median_arr)
print("Standard Deviation:", std_arr)

# Array manipulations
arr = np.array([[1, 2, 3], [4, 5, 6]])

reshaped_arr = arr.reshape((3, 2))
transposed_arr = arr.T
flattened_arr = arr.flatten()

print("Reshaped Array:\n", reshaped_arr)
print("Transposed Array:\n", transposed_arr)
print("Flattened Array:", flattened_arr)

# Mathematical functions
arr = np.array([1, 4, 9, 16])

sqrt_arr = np.sqrt(arr)
exp_arr = np.exp(arr)
log_arr = np.log(arr)

print("Square Root:", sqrt_arr)
print("Exponential:", exp_arr)
print("Logarithm:", log_arr)



#Example
import numpy as np

# Creating an array
arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20]])

# Indexing
print("Element at (1, 2):", arr[1, 2])
print("Element at (-1, -1):", arr[-1, -1])

# Slicing
print("First two rows:\n", arr[:2])
print("First two columns:\n", arr[:, :2])
print("Subarray:\n", arr[:2, :2])

# Boolean indexing
print("Elements greater than 10:\n", arr[arr > 10])

# Fancy indexing
print("First and third row:\n", arr[[0, 2]])
print("First and third column:\n", arr[:, [0, 2]])

#output
Element at (1, 2): 8
Element at (-1, -1): 20
First two rows:
 [[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
First two columns:
 [[ 1  2]
 [ 6  7]
 [11 12]
 [16 17]]
Subarray:
 [[ 1  2]
 [ 6  7]]
Elements greater than 10:
 [11 12 13 14 15 16 17 18 19 20]
First and third row:
 [[ 1  2  3  4  5]
 [11 12 13 14 15]]
First and third column:
 [[ 1  3]
 [ 6  8]
 [11 13]
 [16 18]]
