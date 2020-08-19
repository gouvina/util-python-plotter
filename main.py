#!/usr/bin/env python

### DEPENDENCIES
### ------------------
import sys
import const
import reader
import plotter

### MAIN METHODS
### -------------------

if __name__ == "__main__":
    
    # 1. Read parameters
    path = sys.argv[1]
    try:
        plot_type = int(sys.argv[2])
        if plot_type == 0:
            plot_type = const.PlotOps.CURVE
        elif plot_type == 1:
            plot_type = const.PlotOps.DOTS
        elif plot_type == 2:
            plot_type = const.PlotOps.BARS
        elif plot_type == 3:
            plot_type = const.PlotOps.BOX
    except:
        plot_type = const.PlotOps.CURVE
    
    # 2. Read data
    data = reader.read_data(path)

    # 3. Generate metadata
    meta = {
        'title': '',
        'xlabel': 'k',
        'ylabel': 'PSNR (dB)',
        'colors': [const.COLORS[1], const.COLORS[0], const.COLORS[2]],
        'labels': ['δ = 0.05', 'δ = 0.10', 'δ = 0.35'],
        'hlines': [18.58, 15.59, 10.15],
        'xmin': 0,
        'xmax': 8
    }

    # 4. Plot data
    plotter.plot(data, meta, plot_type)
