# 02-12-2020
# following along to a video showing how to implement simple neural network


import numpy as np

def sigmoid(x):

    return 1 / (1  + np.exp(-x))

    # training input data

training_input_data = np.array([0,1,0],
                               [1,1,1],
                               [1,0,1],
                               [0,1,0])

training_output_data = np.array([[0,1,1,0]]).T

print('Random starting synaptic weights: ')
print(synaptic_weights)

for iteration in range(1):

    input_layer = training_inputs

    outputs = sigmoid(np.dot(training))