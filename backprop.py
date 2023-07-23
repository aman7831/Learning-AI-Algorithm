import numpy as np

# Define the activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Define the input and output data
inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
outputs = np.array([[0, 1, 1, 0]]).T

# Define the weights and biases
weights1 = 2 * np.random.random((3, 4)) - 1
weights2 = 2 * np.random.random((4, 1)) - 1
bias1 = 2 * np.random.random((1, 4)) - 1
bias2 = 2 * np.random.random((1, 1)) - 1

# Train the network for 1000 iterations
for i in range(1000):
    # Perform a forward pass
    layer1 = sigmoid(np.dot(inputs, weights1) + bias1)
    layer2 = sigmoid(np.dot(layer1, weights2) + bias2)

    # Compute the error
    error = outputs - layer2

    # Compute the derivative of the error with respect to the output
    delta2 = error * sigmoid_derivative(layer2)

    # Compute the error for layer 1
    error_layer1 = delta2.dot(weights2.T)

    # Compute the derivative of the error with respect to layer 1
    delta1 = error_layer1 * sigmoid_derivative(layer1)

    # Update the weights and biases
    weights2 += layer1.T.dot(delta2)
    weights1 += inputs.T.dot(delta1)
    bias2 += np.sum(delta2, axis=0, keepdims=True)
    bias1 += np.sum(delta1, axis=0, keepdims=True)

# Print the final outputs
print(layer2)
