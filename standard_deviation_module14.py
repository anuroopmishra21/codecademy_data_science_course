import numpy as np
from data import nba_data, okcupid_data
nba_variance = np.var(nba_data)
okcupid_variance = np.var(okcupid_data)
nba_standard_deviation = nba_variance**0.5
okcupid_standard_deviation = okcupid_variance**0.5
print("The standard deviation of the NBA dataset is " +str(nba_standard_deviation))
print("The standard deviation of the OkCupid dataset is " + str(okcupid_standard_deviation))

import numpy as np
from data import nba_data, okcupid_data
nba_standard_deviation = np.std(nba_data)
okcupid_standard_deviation = np.std(okcupid_data)
print("The standard deviation of the NBA dataset is " +str(nba_standard_deviation))
print("The standard deviation of the OkCupid dataset is " + str(okcupid_standard_deviation))

import numpy as np
from data import nba_data, okcupid_data
nba_mean = np.mean(nba_data)
okcupid_mean = np.mean(okcupid_data)
nba_standard_deviation = np.std(nba_data)
okcupid_standard_deviation = np.std(okcupid_data)
nba_difference = 65-nba_mean
okcupid_difference = 65-okcupid_mean
num_nba_deviations = nba_difference/nba_standard_deviation
num_okcupid_deviations = okcupid_difference/okcupid_standard_deviation
print("Your basketball player is " + str(num_nba_deviations) + " standard deviations away from the mean of NBA player heights\n")
print("Your basketball player is " + str(num_okcupid_deviations) + " standard deviations away from the mean of OkCupid profile heights")
