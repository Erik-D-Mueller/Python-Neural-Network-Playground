# 02-12-2020
# following along to a video showing how to implement simple neural network

import numpy as np

def sigmoid(x):
    return 1 / (1  + np.exp(-x))

 # training input data
training_input_data = np.array([0,0,1],
                               [1,1,1],
                               [1,0,1],
                               [0,1,1]])

training_output_data = np.array([[0,1,1,0]]).T
