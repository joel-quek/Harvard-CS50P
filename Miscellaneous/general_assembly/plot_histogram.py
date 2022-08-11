import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statistics

hist_dataset = pd.read_csv('C:\\Users\\G\Desktop\\General Assembly\\GA Project\\CSV\\duration.csv', encoding='unicode_escape') # output type = pandas dataframe
#hist_dataset = pd.read_csv('C:\\Users\\G\Desktop\\funded_perc.csv', encoding='unicode_escape') # funded percentage
backers = hist_dataset['duration'] # output type = pandas series

plt.figure(figsize=(20,20))

plt.title('Duration Histogram', fontsize=15) #Pledged
plt.xlabel('Duration')
plt.ylabel('Count')
#plt.title('Funded Percentage', fontsize=15) # funded percentage

sns.histplot(data=hist_dataset,binrange=[0,100]) # pledged dataset
#sns.histplot(data=hist_dataset,binrange=[0,1.5]) # funded percentage dataset
# ----------------------------------------------------------------------------------

median_backers = statistics.median(backers)
mean_backers = statistics.mean(backers)

color = '#ff5733'
color2 = '#3355ff'

plt.axvline(median_backers, color = color, label = 'Duration Median', linewidth = 2)
plt.axvline(mean_backers, color = color2, label = 'Duration Mean', linewidth = 2)

# -----------------------------------------------------------------------------------
plt.show()