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
    filename = sys.argv[1]
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
    data = reader.read_data(filename)

    # 3. Generate metadata
    meta = {
        'title': 'Corrida Ej2 - Boxplot',
        'xlabel': 'Tamaño (N)',
        'ylabel': 'Tiempo (ms)',
        'colors': [const.COLORS[1], const.COLORS[1], const.COLORS[0], const.COLORS[0]],
        'labels': ['Vector (min)', 'Vector (max)', 'Matriz (min)', 'Matriz (max)']
    }

    # 4. Plot data
    plotter.plot(data, meta, plot_type)
