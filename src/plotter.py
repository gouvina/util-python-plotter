# DEPENDENCIES
# -----------------------------------------------------------------------------------------------
# General dependencies
import numpy as np
import matplotlib.pyplot as plt
# Local dependencies
from src.constants.enums import PlotOps

# AUX METHODS
# -----------------------------------------------------------------------------------------------

def plotCurves(data, meta):

    plt.figure(figsize=(12,6)) 
    plt.xlabel(meta['xlabel'])
    plt.ylabel(meta['ylabel'])
    plt.title(meta['title'])

    for index, (x,y) in enumerate(data):
        plt.plot(x, y, alpha=0.8, label=meta['labels'][index], color=meta['colors'][index])
    
    plt.legend(loc="upper left")
    plt.show()

def plotScatter(data, meta):

    plt.figure(figsize=(12,6)) 
    plt.xlabel(meta['xlabel'])
    plt.ylabel(meta['ylabel'])    
    plt.title(meta['title'])

    for index, (x,y) in enumerate(data):
        plt.scatter(x, y, alpha=0.8, edgecolors='none', label=meta['labels'][index], color=meta['colors'][index])
        
    plt.legend(loc="upper left")
    plt.show()

def plotBars(data, meta):

    plt.figure(figsize=(12,6)) 
    plt.xlabel(meta['xlabel'])
    plt.ylabel(meta['ylabel'])    
    plt.title(meta['title'])

    index = 0
    for x,y in data:
        plt.bar(x,y, align='center', alpha=0.8, color=meta['colors'][index], label=meta['labels'][index])
        index = index + 1
    
    plt.legend(loc="upper left")
    plt.show()

def plotMultibars(data, meta):

    plt.figure(figsize=(12,6)) 
    plt.xlabel(meta['xlabel'])
    plt.ylabel(meta['ylabel'])    
    plt.title(meta['title'])

    bars = len(data[0])
    y_pos = np.arange(bars)

    for index, _ in enumerate(data):
        plt.bar(y_pos + 0.2 * index, data[index], width=0.2, align='center', alpha=0.8, color=meta['colors'][index], label= meta['labels'][index])
    
    plt.xticks(y_pos, meta['ticks'])
    plt.legend(loc="upper left")
    plt.show()

# MAIN METHODS
# -----------------------------------------------------------------------------------------------

def plot(data, meta, plot_type):

    if plot_type == PlotOps.CURVE:
        plotCurves(data, meta)
    elif plot_type == PlotOps.DOTS:
        plotScatter(data, meta)
    elif plot_type == PlotOps.BARS:
        plotBars(data, meta)
    elif plot_type == PlotOps.MULTIBARS:
        plotMultibars(data, meta)



