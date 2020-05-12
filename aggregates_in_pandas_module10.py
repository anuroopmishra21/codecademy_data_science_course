import codecademylib
import pandas as pd
orders = pd.read_csv('orders.csv')
print(orders.head(10))
most_expensive = orders.price.max()
num_colors = orders.shoe_color.nunique()

import codecademylib
import pandas as pd
orders = pd.read_csv('orders.csv')
pricey_shoes = orders.groupby('shoe_type').price.max()
print(pricey_shoes)
print(type(pricey_shoes))

import codecademylib
import pandas as pd
orders = pd.read_csv('orders.csv')
pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
print(pricey_shoes)
print(type(pricey_shoes))

import codecademylib
import numpy as np
import pandas as pd
orders = pd.read_csv('orders.csv')
cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x:np.percentile(x,25)).reset_index()
print(cheap_shoes)

import codecademylib
import numpy as np
import pandas as pd
orders = pd.read_csv('orders.csv')
shoe_counts = orders.groupby(['shoe_type','shoe_color']).id.count().reset_index()
print(shoe_counts)

import codecademylib
import numpy as np
import pandas as pd
orders = pd.read_csv('orders.csv')
shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()
shoe_counts_pivot = shoe_counts.pivot(
  columns = 'shoe_color',
  index = 'shoe_type',
  values = 'id'
).reset_index()
print(shoe_counts_pivot)

import codecademylib
import pandas as pd
user_visits = pd.read_csv('page_visits.csv')
print(user_visits.head())
click_source = user_visits.groupby('utm_source').id.count().reset_index()
print(click_source)
click_source_by_month = user_visits.groupby(['utm_source','month']).id.count().reset_index()
click_source_by_month_pivot = click_source_by_month.pivot(
  columns = 'month',
  index = 'utm_source',
  values = 'id'
).reset_index()
print(click_source_by_month_pivot)
