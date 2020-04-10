### DEPENDENCIES
### ------------------
import numpy as np
import matplotlib.pyplot as plt
from const import PlotOps

### AUX METHODS
### ------------------

def plotCurves(data, meta):

    plt.figure(figsize=(12,6)) 
    plt.xlabel(meta['xlabel'])
    plt.ylabel(meta['ylabel'])    
    plt.title(meta['title'])

    x_values, y_values = data
    for index, column in enumerate(y_values):
        plt.plot(x_values, column, alpha=0.8, label=meta['labels'][index], color=meta['colors'][index])
    
    plt.legend(loc="upper left")
    plt.show()

def plotScatter(data, meta):

    plt.figure(figsize=(12,6)) 
    plt.xlabel(meta['xlabel'])
    plt.ylabel(meta['ylabel'])    
    plt.title(meta['title'])

    x_values, y_values = data
    for index, column in enumerate(y_values):
        plt.scatter(x_values, column, alpha=0.8, edgecolors='none', label=meta['labels'][index], color=meta['colors'][index])
    
    plt.legend(loc="upper left")
    plt.show()


def plotBox(data, meta):
    return 0

### MAIN METHODS
### ------------------

def plot(data, meta, plot_type):

    if plot_type == PlotOps.CURVE:
        plotCurves(data, meta)
    elif plot_type == PlotOps.DOTS:
        plotScatter(data, meta)
    elif plot_type == PlotOps.BOX:
        plotBox(data, meta)
