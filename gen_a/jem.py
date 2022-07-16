import pandas as pd
from matplotlib import pyplot as plt
import statistics

data = pd.read_csv('sheet.csv') # data is a pandas core frame dataframe
shef = data['Small'] # shef is a pandas core frame series
mastershef=data['Large']

print(type(data))
print(type(shef))
print(shef)
print(mastershef)