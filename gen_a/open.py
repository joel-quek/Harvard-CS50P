import matplotlib as mpl # for plotting
# https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
import matplotlib.pyplot as plt
import numpy as np # for arrays
import pandas as pd # for opening files
from pathlib import Path # for opening files
import csv, sys # for csv
from tabulate import tabulate
# from __future__ import division
# --------------------------------------------------------------------------------------------------------
# Open CSV
# https://stackoverflow.com/questions/66499795/how-do-i-read-in-a-csv-file-from-my-desktop-in-python
filename = input("Filename: ")
file = open(filename)
reader = csv.reader(file)
data=list(reader)
print(data)
# print(tabulate(data, tablefmt="grid", headers = "firstrow"))

# i cant open data.csv or data2.csv because the dataset is too large
# --------------------------------------------------------------------------------------------------------
# Remove empty rows from csv
# https://stackoverflow.com/questions/4521426/delete-blank-rows-from-csv

# --------------------------------------------------------------------------------------------------------
# Pull out relevant column as an array
pledge = []
for row in data:
    pledge.append(row[1])
pledge.remove(pledge[0])

print(pledge)
# --------------------------------------------------------------------------------------------------------
# Plot the array as a histogram
# missing code refer to hist.py (https://stackoverflow.com/questions/43264883/plotting-a-numpy-array-as-a-histogram)
# use bin to group cumulative data https://www.youtube.com/watch?v=P0aqnNv9arA


# --------------------------------------------------------------------------------------------------------
# Calculate mean and determine if data is normally distributed


# --------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------
# C:\Users\s8936637b\Desktop\data.csv
# data3.csv
# ANSWERS:
# Mean = 4980.74979