# DEPENDENCIES
# -----------------------------------------------------------------------------------------------
# General dependencies
import sys
# Local dependencies
import src.constants.colors as colors
import src.constants.enums as enums
import src.reader as reader
import src.formatter as formatter
import src.plotter as plotter

### MAIN METHOD
# -----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    
    # 1. Read parameters
    filename = sys.argv[1]
    plot_type = formatter.parse_plot_type(int(sys.argv[2]))

    # 2. Read data
    data, labels = reader.read_data(filename)

    # 3. Generate metadata
    meta = {
        'title': formatter.parse_filename(filename),
        'colors': [colors.ORANGE, colors.BLUE, colors.RED, colors.CYAN, colors.YELLOW, colors.GREEN, colors.AQUAMARINE, colors.LILY],
    }

    # 4. Format data
    if plot_type == enums.PlotOps.CURVE:

        # 4.1. Get dataset's attributes
        labels = formatter.get_attributes(labels)

        # 4.2. Get dataset formatted by classes
        data = formatter.count_data_by_attribute(data, labels)

        # 4.3. Format metadata
        meta['xlabel'] = 'Values'
        meta['ylabel'] = 'Amount of samples'
        meta['labels'] = labels

    elif plot_type == enums.PlotOps.DOTS:
        
        # 4.1. Get dataset's attributes
        labels = formatter.get_attributes(labels)

        # 4.2. Get dataset formatted by classes
        data = formatter.count_data_by_attribute(data, labels)

        # 4.3. Format metadata
        meta['xlabel'] = 'Values'
        meta['ylabel'] = 'Amount of samples'
        meta['labels'] = labels

    elif plot_type == enums.PlotOps.BARS:

        # 4.1. Get dataset's classes
        labels = formatter.get_classes(data)

        # 4.2. Get dataset formatted by classes
        data = formatter.count_data_by_class(data, labels)

        # 4.3. Format metadata
        meta['xlabel'] = 'Classes'
        meta['ylabel'] = 'Examples per class'
        meta['labels'] = labels

    elif plot_type == enums.PlotOps.MULTIBARS:

        # 4.1. Get dataset's classes
        classes = formatter.get_classes(data)

        # 4.2. Get dataset's attributes
        labels = formatter.get_attributes(labels)

        # 4.3. Get dataset formatted by classes
        data = formatter.count_max_by_attribute(data, classes, labels)

        # 4.4. Format metadata
        meta['xlabel'] = 'Attributes'
        meta['ylabel'] = 'Values'
        meta['labels'] = labels
        meta['ticks'] = classes

    # 5. Plot data
    plotter.plot(data, meta, plot_type)
