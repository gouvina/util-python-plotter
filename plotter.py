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

def plotBars(data, meta):

    plt.figure(figsize=(12,6)) 
    plt.xlabel(meta['xlabel'])
    plt.ylabel(meta['ylabel'])    
    plt.title(meta['title'])

    x_values, y_values = data
    width = 0.2
    
    y_pos = np.arange(len(x_values))
    y_pos_full = [y_pos - 0.4, y_pos - 0.2, y_pos, y_pos + 0.2]
    for index, column in enumerate(y_values):
        plt.bar(y_pos_full[index], y_values[index], width=width, align='center', alpha=0.8, color=meta['colors'][index], label= meta['labels'][index])
    plt.xticks(y_pos, x_values.astype(int))
    
    plt.legend(loc="upper left")
    plt.show()

def plotBox(data, meta):
    plt.figure(figsize=(12,6)) 
    plt.xlabel(meta['xlabel'])
    plt.ylabel(meta['ylabel'])    
    plt.title(meta['title'])

    x_values, y_values = data
    plt.boxplot(y_values[0], showfliers=False)
    plt.xticks(np.arange(1, len(x_values) + 1), x_values.astype(int))

    plt.show()

### MAIN METHODS
### ------------------

def plot(data, meta, plot_type):

    if plot_type == PlotOps.CURVE:
        plotCurves(data, meta)
    elif plot_type == PlotOps.DOTS:
        plotScatter(data, meta)
    elif plot_type == PlotOps.BARS:
        plotBars(data, meta)
    elif plot_type == PlotOps.BOX:
        plotBox(data, meta)
