# How-To Guide

This guide shows you how to install this software, and how use it to analyse data about space walks.

## How to install the software

To install Spacewalks, either clone the git repository (recommended):

- Open the command line terminal or powershell, and navigate to the directory you want to install in.

- Then type: 

```
git clone git@github.com:Fehings/SpaceWalk.git
cd spacewalks
```

- Install the necessary dependencies:
```
python3 -m pip install pandas==2.2.2 matplotlib==3.8.4 numpy==2.0.0 pytest==7.4.2
```

- To ensure everything is working correctly, run the tests using pytest.

```
python3 -m pytest
```
or click on the <>code button and select `download zip`, then unzip in the location you want to install
and follow the dependency installation and testing above. This will mean your code isn't being version 
controlled though so we recommend creating a git repository to keep track of changes if you do this!


## Using it to analyse NASA data

Run the main script from the terminal with:

```
Python eva_data_analysis.py input_data.json output_filename.csv
```

Where you replace `input_data.json` with your input eva data, and the `output_filename.csv` 
is replaced with whatever filename you want to save as, with a csv extension.

e.g.
```
Python eva_data_analysis.py data/eva-data.json results/eva-data.csv
```

should work with the included demo data. 


## Changing the default output destination

If you pass the output file from the command line then you can call the output whatever you want!

E.g. if you want to send the output to a 'new_analysis' folder, but to run with the included data, you could
 modify the command you run to be:
 ```
Python eva_data_analysis.py data/eva-data.json new_analysis/eva-data.csv
```





## Extending the code