import numpy as np
import pandas as pd
from scipy import stats
brooklyn_one_bed = pd.read_csv('brooklyn-one-bed.csv')
brooklyn_price = brooklyn_one_bed['rent']
manhattan_one_bed = pd.read_csv('manhattan-one-bed.csv')
manhattan_price = manhattan_one_bed['rent']
queens_one_bed = pd.read_csv('queens-one-bed.csv')
queens_price = queens_one_bed['rent']
brooklyn_mean = np.mean(brooklyn_price)
manhattan_mean = np.mean(manhattan_price)
queens_mean = np.mean(queens_price)
brooklyn_median = np.median(brooklyn_price)
manhattan_median = np.median(manhattan_price)
queens_median = np.median(queens_price)
brooklyn_mode = stats.mode(brooklyn_price)
manhattan_mode = stats.mode(manhattan_price)
queens_mode = stats.mode(queens_price)
print("The mean price in Brooklyn is " + str(round(brooklyn_mean, 2)))
print("The mean price in Manhattan is " + str(round(manhattan_mean, 2)))
print("The mean price in Queens is " + str(round(queens_mean, 2)))
print("The median price in Brooklyn is " + str(brooklyn_median))
print("The median price in Manhattan is " + str(manhattan_median))
print("The median price in Queens is " + str(queens_median))
print("The mode price in Brooklyn is " + str(brooklyn_mode[0][0]) + " and it appears " + str(brooklyn_mode[1][0]) + " times out of " + str(len(brooklyn_price)))
print("The mode price in Manhattan is " + str(manhattan_mode[0][0]) + " and it appears " + str(manhattan_mode[1][0]) + " times out of " + str(len(manhattan_price)))
print("The mode price in Queens is " + str(queens_mode[0][0]) + " and it appears " + str(queens_mode[1][0]) + " times out of " + str(len(queens_price)))
