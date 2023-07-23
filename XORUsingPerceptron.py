import numpy as np

# Define the activation function
def step_function(x):
    if x >= 0:
        return 1
    else:
        return 0

# Define the XOR function using two AND functions and an OR function
def XOR(x1, x2):
    s1 = step_function(np.sum(np.array([x1, x2]) * np.array([-0.5, -0.5])) - 0.7)
    s2 = step_function(np.sum(np.array([x1, x2]) * np.array([0.5, 0.5])) - 0.7)
    return step_function(np.sum(np.array([s1, s2]) * np.array([0.5, 0.5])) - 0.7)

# Test the XOR function
print(XOR(0, 0)) # Output: 0
print(XOR(0, 1)) # Output: 1
print(XOR(1, 0)) # Output: 1
print(XOR(1, 1)) # Output: 0
