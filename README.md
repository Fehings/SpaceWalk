# Spacewalks

## Overview 
Spacewalks is a Python analysis tool for researchers to generate visualisations
 and statistical summaries of NASA's extravehicular activity datasets.

 ## Features 
 Key features of Spacewalks:

 - Generates a CVS table of summary statistics of extravehicular activity crew 
 sizes.
 - Generates a line plot to show the cumulative duration of space walks over time.

 ## Prerequisites

 Spacewalks was developed using Python 3.12.

 To install and run Spacewalks you will need to have Python >-3.12.

 You will also need the following libraries:

 - [NumPy](https://www.numpy.org) >=2.0.0 - Spacewalks' test suite uses Numpy's statistical functions.

- [Matplotlib](https://matplotlib.org/stable/index.html) >= 3.0.0 - Spacewalks uses Matplotlib to make plots.
- [pytest](https://docs.pytest.org/en/8.2.x/#) >= 8.2.0 - Spavewalks uses Pytest for its test suite.
- [pandas](https://pandas.pydata.org) >= 2.2.0 - Used for data frame manipulation and loading/saving data.

## Installation Instructions

To install Spacewalks, either clone the git repository (recommended):

- Open the command line terminal or powershell, and navigate to the directory you want to install in.

- Then type: `git clone git@github.com:Fehings/SpaceWalk.git`

or click on the <>code button and select `download zip`, then unzip in the location you want to install.

## Usage example

Run the main script from the terminal with:

`Python eva_data_analysis.py input_data.json output_filename.csv`

Where you replace `input_data.json` with your input eva data, and the `output_filename.csv` 
is replaced with whatever filename you want to save as, with a csv extension.

e.g.
`Python eva_data_analysis.py data/eva-data.json results/eva-data.csv`

should work with the included demo data. 

