### DEPENDENCIES
### ------------------
import json
import os
import numpy as np
import pandas as pd

from pathlib import Path

### MAIN METHODS
### -------------------

# Reads whatever is on 'path'
#  - If file.csv it returns it as a numpy array
#  - If it's a directory it reads all .csvs inside and returns a matrix composed of an array per file
def read_data(path):
    if os.path.isdir(path):
        files = find_files(path, '.csv')
        data = [read_file(filename) for filename in files]
    else: # isfile
        data = read_file(path)
    
    return data

def find_files(path, suffix):
    return sorted([filename for filename in Path(path).rglob(f"*{suffix}")])

# Reads a .csv file and returns it as a numpy array
def read_file(filename):
    data = pd.read_csv(filename, header=None)
    return process_data(data.to_numpy()) # Just change this method's inner code

# Process data in the desired way
def process_data(data):

    x_values = data[:, 0]
    y_values = data[:, 1]

    return x_values, y_values