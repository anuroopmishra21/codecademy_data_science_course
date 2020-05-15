import pandas as pd
from matplotlib import pyplot as plt
restaurants=pd.read_csv('restaurants.csv')
print(restaurants.head())
cuisine_options_count=restaurants.cuisine.nunique()
cuisine_counts=restaurants.groupby('cuisine').name.count().reset_index()
print(cuisine_options_count)
print(cuisine_counts)

import codecademylib3
from matplotlib import pyplot as plt
import pandas as pd
restaurants = pd.read_csv('restaurants.csv')
cuisine_counts = restaurants.groupby('cuisine').name.count().reset_index()
cuisines = cuisine_counts.cuisine.values
counts = cuisine_counts.name.values
plt.pie(counts,autopct='%d%%',labels=cuisines)
plt.title('Number of restaurants for each cuisine')
plt.axis('equal')
plt.show()

import codecademylib
from matplotlib import pyplot as plt
import pandas as pd
orders = pd.read_csv('orders.csv')
print orders.head()
orders['month'] = orders.date.apply(lambda x: x.split('-')[0])
print orders.head()
avg_order = orders.groupby('month').price.mean().reset_index()
std_order = orders.groupby('month').price.std().reset_index()

import codecademylib
from matplotlib import pyplot as plt
import pandas as pd
orders = pd.read_csv('orders.csv')
orders['month'] = orders.date.apply(lambda x: x.split('-')[0])
avg_order = orders.groupby('month').price.mean().reset_index()
std_order = orders.groupby('month').price.std().reset_index()
ax=plt.subplot()
bar_heights = [i for i in avg_order.price]
bar_errors = [i for i in std_order.price]
months = ['April','May','June','July','August','September']
plt.bar(range(len(bar_heights)),bar_heights,yerr=bar_errors,capsize=5)
ax.set_xticks(range(len(bar_heights)))
ax.set_xticklabels(months)
plt.ylabel('Average Price')
plt.xlabel('Months')
plt.title('Average Price in Each Month')
plt.show()

import codecademylib
from matplotlib import pyplot as plt
import pandas as pd
orders = pd.read_csv('orders.csv')
customer_amount = orders.groupby('customer_id').price.sum().reset_index()
print(customer_amount.head())
plt.hist(customer_amount.price.values,range=(0, 200), bins=40)
plt.xlabel('Total Spent')
plt.ylabel("Number of Customers")
plt.title('Customer Expenditure Over 6 Months')
plt.show()
