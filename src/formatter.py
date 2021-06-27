# DEPENDENCIES
# -----------------------------------------------------------------------------------------------
# General dependencies
import ntpath
import numpy as np
# Local dependencies
import src.constants.enums as enums

# AUX METHODS
# -----------------------------------------------------------------------------------------------

# Read plot type as an int, parse it to enum
def parse_plot_type(plot_type):
    type = enums.PlotOps.CURVE
    try:
        if plot_type == 0:
            type = enums.PlotOps.CURVE
        elif plot_type == 1:
            type = enums.PlotOps.DOTS
        elif plot_type == 2:
            type = enums.PlotOps.BARS
        elif plot_type == 3:
            type = enums.PlotOps.MULTIBARS
        else:
            type = enums.PlotOps.CURVE
    except:
        type = enums.PlotOps.CURVE
    return type

# Parse file name without extension from a file path
def parse_filename(path):
    head, tail = ntpath.split(path)
    return tail.split('.')[0] or ntpath.basename(head).split('.')[0]

# MAIN METHODS
# -----------------------------------------------------------------------------------------------

# Count samples of each class
def count_data_by_class(data, classes):

    # Return result as list
    result = []

    # Filter data for each label
    for c in classes:
        length = data[data[:, -1] == c].size
        result.append((c, length))

    return result

# Check max for each attribute
def count_max_by_attribute(data, classes, attributes):

    # Return result as list
    result = []
    result_aux = []

    # Filter data for each class and attribute
    for index, _ in enumerate(attributes):
        for c in classes:
            data_by_class = data[data[:,-1] == c]
            max = np.amax(data_by_class[:, index])
            result_aux.append(max)
        result.append(result_aux)
        result_aux = []

    return result

# Count samples of each value for each attribute
def count_data_by_attribute(data, attributes):

    # Return result as list
    result = []
    result_x = []
    result_y = []

    # Filter data for each class and attribute
    for index, attribute in enumerate(attributes):
        column = data[:, index]
        values = np.unique(column)
        values = np.sort(values)
        for value in values:
            amount = column[column == value].size
            result_x.append(value)
            result_y.append(amount)
        result_x = np.asarray(result_x, dtype=np.float32)
        result_y = np.asarray(result_y, dtype=np.float32)
        result.append((result_x, result_y))
        result_x = []
        result_y = []

    return result

# Get classes from last column from data
def get_classes(data):
    return np.unique(data[:, -1])

# Get attributes from all but last columns
def get_attributes(data):
    return data[:-1]