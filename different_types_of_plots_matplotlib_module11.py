import codecademylib
from matplotlib import pyplot as plt
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]
plt.bar(range(len(drinks)),sales)
plt.show()

import codecademylib
from matplotlib import pyplot as plt
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]
plt.bar(range(len(drinks)), sales)
ax=plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)
plt.show()

import codecademylib
from matplotlib import pyplot as plt
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(drinks) # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element
             in range(d)]
plt.bar(store1_x,sales1)
n = 2  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(drinks) # Number of sets of bars
w = 0.8 # Width of each bar
store2_x = [t*element + w*n for element
             in range(d)]
plt.bar(store2_x,sales2)
plt.show()

import codecademylib
from matplotlib import pyplot as plt
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
plt.bar(range(len(drinks)),sales1)
plt.bar(range(len(drinks)),sales2,bottom = sales1)
plt.legend(['Location 1','Location 2'])
plt.show()

import codecademylib
from matplotlib import pyplot as plt
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]
plt.bar(range(len(drinks)),ounces_of_milk,yerr=error,capsize=5)
plt.show()

import codecademylib
from matplotlib import pyplot as plt
months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]
ax=plt.subplot()
plt.plot(months,revenue)
ax.set_xticks(months)
ax.set_xticklabels(month_names)
y_lower = [i*0.9 for i in revenue]
y_upper = [i*1.1 for i in revenue]
plt.fill_between(months,y_lower,y_upper,alpha=0.2)
plt.show()

import codecademylib
from matplotlib import pyplot as plt
import numpy as np
payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]
plt.pie(payment_method_freqs)
plt.axis('equal')
plt.show()

import codecademylib
from matplotlib import pyplot as plt
payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]
plt.pie(payment_method_freqs,autopct='%0.1f%%')
plt.axis('equal')
plt.legend(payment_method_names)
plt.show()

import codecademylib
from matplotlib import pyplot as plt
from script import sales_times
plt.hist(sales_times,bins = 20)
plt.show()

import codecademylib
from matplotlib import pyplot as plt
from script import sales_times1
from script import sales_times2
plt.hist(sales_times1, bins=20,alpha=0.4,normed=True)
plt.hist(sales_times2,bins=20,alpha=0.4,normed=True)
plt.show()
