### DEPENDENCIES
### ------------------
from enum import Enum

### CONSTANTS
### ------------------

# Colors
COLORS = ['#f58231', '#4363d8', '#e6194B', '#3cb44b', '#469990', '#ffe119', '#000075', '#bfef45', '#42d4f4', '#9F8BE5', '#9400FF']

# Plot types
class PlotOps(Enum):
    CURVE = 0
    DOTS = 1
    BARS = 2
    BOX = 3