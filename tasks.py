import numpy

# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.

# Task 1: 
# Instructions:
#Write a function that takes one numeric argument as input. 
#If the number is larger than zero, the function should return 1, otherwise is should return -1.
#The name of the function should be step

# Your code here:
# -----------------------------------------------

def step(x):
    try:
        x = float(x)
    except (ValueError, TypeError):
        raise ValueError("Input must be numeric")
    if x > 0:
        return 1
    else:
        return -1

print(step(3))
# -----------------------------------------------


# Task 2:
# Instructions:
#Write a function that takes in two arguments: a numpy array, and an integer (call argument "cutoff" and set default to 0).
#The function should return a numpy array of the same length, with all elements smaller than the cutoff being set to cutoff).
#The name of the function should be ReLu


# Your code here:
# -----------------------------------------------
def ReLu(arr, cutoff = 0):
    arr = arr.copy()  # make a copy of arr to avoid modifying the original array
    for i in range(len(arr)):
        if arr[i] < cutoff:
            arr[i] = cutoff
    return arr


#   arr[arr < cutoff] = cutoff also works (True = cutoff value, False = original value)
# -----------------------------------------------


# Task 3:
# Instructions:
#Write a function that takes in a two-dimensional numpy array of size (n, p) and a one-dimensional numpy array of size p.
#The function should start by multiplying the two numpy arrays (matrix multiplication).
#Next, apply the ReLu function from above to the resulting matrix and return the result.
#Name the function neural_net_layer

# Your code here:
# -----------------------------------------------

def neural_net_layer(td_arr, od_arr):
  if td_arr.shape[1] != len(od_arr):
     raise ValueError("Number of columns must match length of the 1D array")
  x = np.dot(td_arr, od_arr)
  return ReLu(x)


# shape[0] = number of rows, shape[1] = number of columns of array
# np.dot(A, B) (or A @ B) = matrix multiplication
# Matrix multiplication: columns of 1st matrix = rows of 2nd matrix.
# A 1D array has no rows/columns, so its length just has to match the columns.

# ------------------------------------------