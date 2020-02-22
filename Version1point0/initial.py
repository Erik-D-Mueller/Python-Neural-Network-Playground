# 02-12-2020
# following along to a video showing how to implement simple neural network

import numpy as np

def sigmoid(x):

    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):

    return x * (1 - x)
    # training input data

training_input_data = np.array([
    [0,1,0],
    [1,1,1],
    [1,0,1],
    [0,1,0]])

training_output_data = np.array([[0,1,1,0]]).T

synaptic_weights = 2 * np.random.random((3,1)) - 1

print('Initial Random starting synaptic weights: ')
print(synaptic_weights)

for iteration in range(500000):

    input_layer = training_input_data

    outputs = sigmoid(np.dot(training_input_data,synaptic_weights))

    error = training_output_data - outputs

    adjustments = error + sigmoid_derivative(outputs)

    synaptic_weights += np.dot(input_layer.T, adjustments)

print('Synaptic weights after training')
print(synaptic_weights)

print('Outputs after training')
print(outputs)
