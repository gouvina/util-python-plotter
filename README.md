# Plotter (Python)
Base Project for generating personalized plots using Python and Matplotlib:

## Setup
1 - (Optional) Generate virtual environment: <br>
`python -m venv env` <br>

2 - (Optional) Activate virtual environment: <br>
`env/Scripts/activate.bat` (Windows)<br>
`./env/Scripts/activate` (Unix)<br>

3 - Install requirements: <br>
`pip install -r requirements.txt` <br>

## Usage
`python main.py <path> <plot_type>` <br>

Being the two parameters:
1. `path`: path to a CSV file that represents the dataset to analyze.
2. `plot_type`: an integer representing the type of plot to generate, being available the next options:
    - Curves = 0
    - Dots = 1
    - Bars = 2
    - Multibars = 3

 
