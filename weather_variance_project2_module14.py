import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data
#print(london_data.head())
print(len(london_data))
temp = london_data['TemperatureC']
average_temp = np.mean(temp)
temperature_var = np.var(temp)
print(average_temp)
print(temperature_var)
temperature_standard_deviation = np.std(temp)
print(temperature_standard_deviation)
for i in range(1,13):
  month = london_data.loc[london_data['month']==i]['TemperatureC']
  print('The mean of month '+str(i)+' is '+str(np.mean(month)))
  print('The standard deviation of month '+str(i)+' is '+str(np.std(month)))
