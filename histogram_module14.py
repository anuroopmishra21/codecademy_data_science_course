import numpy as np
import pandas as pd
transactions = pd.read_csv("transactions.csv")
times = transactions["Transaction Time"].values
cost = transactions["Cost"].values
min_time = np.amin(times)
max_time = np.amax(times)
range_time = max_time-min_time
print("Earliest Time: " + str(min_time))
print("Latest Time: " + str(max_time))
print("Time Range: " + str(range_time))

import numpy as np
import pandas as pd
days_old_bread = np.array([0, 8, 7, 8, 0, 2, 3, 5, 6, 2])
min_days_old = np.amin(days_old_bread)
max_days_old = np.amax(days_old_bread)
bins=3
bin_range = (max_days_old - min_days_old + 1) / bins
print("Bins: " + str(bins))
print("Bin Width: " + str(bin_range))

import numpy as np
import pandas as pd
days_old_bread = np.array([0, 8, 7, 8, 0, 2, 3, 5, 6, 2])
days_old_012 = 4
days_old_345 = 2
days_old_678 = 4
print("Between 0 and 2 days: " + str(days_old_012))
print("Between 3 and 5 days: " + str(days_old_345))
print("Between 6 and 8 days: " + str(days_old_678))

import numpy as np
import pandas as pd
transactions = pd.read_csv("transactions.csv")
times = transactions["Transaction Time"].values
times_hist = np.histogram(times,range = (0,24),bins=4)
print(times_hist)

import codecademylib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
transactions = pd.read_csv("transactions.csv")
times = transactions["Transaction Time"].values
plt.hist(times,range=(0,24),bins=4)
plt.xlabel('Range of Time')
plt.ylabel('Number of Customers')
plt.title('Frequeny of during the day')
plt.show()

import codecademylib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
transactions = pd.read_csv("transactions.csv")
times = transactions["Transaction Time"].values
plt.hist(times, range=(0, 24), bins=24,  edgecolor="black")
plt.title("Weekday Frequency of Customers")
plt.xlabel("Hours (1 hour increments)")
plt.ylabel("Count")
plt.show()
