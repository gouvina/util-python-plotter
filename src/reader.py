# DEPENDENCIES
# -----------------------------------------------------------------------------------------------
# General dependencies
import numpy as np
import pandas as pd

# AUX METHODS
# -----------------------------------------------------------------------------------------------

# Process data in the desired way (by default do nothing)
def process_data(data):
    return data

# MAIN METHODS
# -----------------------------------------------------------------------------------------------

# Reads 'filename' and returns it as a numpy array
def read_data(filename):
    
    # Read CSV file as DataFrame
    df = pd.read_csv(filename)
    
    # Get column names as list of strings
    columns = list(df.columns.values)
    
    # Get dataset rows as numpy array (and process it if needed)
    data = process_data(df.values)
    
    return data, columns
    
