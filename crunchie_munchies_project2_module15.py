import codecademylib
import numpy as np
calorie_stats = np.genfromtxt('cereal.csv',delimiter = ',')
average_calories = np.mean(calorie_stats)
print(average_calories)
calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)
median_calories = np.median(calorie_stats)
print(median_calories)
fourth_percentile = np.percentile(calorie_stats,4)
more_calories = np.mean(calorie_stats > 60)
print(more_calories)
calorie_std = np.std(calorie_stats)
print(calorie_std)
