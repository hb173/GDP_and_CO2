import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv('https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv')
data_new = data[['Mortality rate, infant (per 1,000 live births)','GDP per capita (constant 2010 US$)','Country Name']]
plt.scatter(data_new['Mortality rate, infant (per 1,000 live births)'], data_new['GDP per capita (constant 2010 US$)'])
plt.show()
