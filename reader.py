### DEPENDENCIES
### ------------------
import json
import numpy as np
import pandas as pd

### MAIN METHODS
### -------------------

# Reads 'filename' and returns it as a numpy array
def read_data(filename):
    data = pd.read_csv(filename, header=None)
    return process_data(data.to_numpy()) # Just change this method's inner code

# Process data in the desired way
def process_data(data):

    #
    x_values = data[:, 0]
    
    #
    y_values = data[:, 1:]

    #    
    y_vector = y_values[:, 0::2]
    y_vector_min = np.amin(y_vector, axis=1)
    y_vector_max = np.amax(y_vector, axis=1)

    #
    y_matrix = y_values[:, 1::2]
    y_matrix_min = np.amin(y_matrix, axis=1)
    y_matrix_max = np.amax(y_matrix, axis=1)

    #return x_values, [y_vector_min, y_vector_max, y_matrix_min, y_matrix_max]
    return x_values, [y_vector.transpose(), y_matrix.transpose()]