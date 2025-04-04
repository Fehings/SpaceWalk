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