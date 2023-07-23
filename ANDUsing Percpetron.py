import numpy as np

# Define the activation function
def step_function(x):
    if x >= 0:
        return 1
    else:
        return 0

# Define the AND function
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    return step_function(tmp)

# Test the AND function
print(AND(0, 0)) # Output: 0
print(AND(0, 1)) # Output: 0
print(AND(1, 0)) # Output: 0
print(AND(1, 1)) # Output: 1
