import codecademylib3
import numpy as np
from matplotlib import pyplot as plt
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")
plt.figure(1)
plt.subplot(211)
plt.hist(flights,range=(0,365),bins=365)
plt.xlabel('Day of the year')
plt.ylabel('Number of flights')
plt.title('Frequency of flights by day')
plt.subplot(212)
plt.hist(in_bloom,range=(0,365),bins=365)
plt.xlabel('Day of the year')
plt.ylabel('Blooming of the flower')
plt.title('Blooming by day')
plt.tight_layout()
plt.show()
