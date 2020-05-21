import numpy as np
from data import dataset
dataset_median = np.median(dataset)
try:
  print("The median of the dataset is " + str(dataset_median) + ".")
except NameError:
  print("You haven't defined dataset_median")
  
import numpy as np
from data import dataset
quartile_one = np.quantile(dataset, 0.25) 
quartile_three = np.quantile(dataset, 0.75)
# Define your variables here:
iqr = quartile_three - quartile_one
distance = 1.5 * iqr
left_whisker = quartile_one - distance
right_whisker = quartile_three  + distance
#Ignore the code below here
try:
  print("The interquartile range of the dataset is " + str(iqr) + ".")
except NameError:
  print("You haven't defined iqr.")
try:
  print("Each whisker should be " + str(distance) + " units away from the edges of the box.")
except NameError:
  print("You haven't defined distance.")
try:
  print("The left whisker should extend to " + str(left_whisker) + " .")
except NameError:
  print("You haven't defined left_whisker.")
try:
  print("The right whisker should extend to " + str(right_whisker) + " .")
except NameError:
  print("You haven't defined right_whisker.")
  
import numpy as np
dataset = [8, 9.5, 10, 10, 8, 11, 15, 5, -2, -1, 10, 10, 6, 8, 9]
quartile_one = np.quantile(dataset, 0.25)
quartile_three = np.quantile(dataset, 0.75)
iqr = quartile_three - quartile_one
left_whisker = quartile_one - 1.5 * iqr
right_whisker = quartile_three + 1.5 * iqr
print("The left whisker extends to " + str(left_whisker))
print("The right whisker extends to " + str(right_whisker))
# Define your variables here:
outlier_one = -2
outlier_two = -1
outlier_three = 15

import codecademylib3_seaborn
import matplotlib.pyplot as plt
from music_data import two_thousand, two_thousand_one, two_thousand_two
plt.boxplot([two_thousand,two_thousand_one,two_thousand_two],labels = ['2000 Songs','2001 Songs','2002 Songs'])
plt.show()
