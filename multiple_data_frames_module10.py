import pandas as pd
orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')
customers = pd.read_csv('customers.csv')
print(orders)
print(products)
print(customers)

import codecademylib
import pandas as pd
orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')
customers = pd.read_csv('customers.csv')
print(orders)
print(products)
print(customers)
order_3_description = 'thing-a-ma-jig'
order_5_phone_number = '112-358-1321'

import codecademylib
import pandas as pd
sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)
sales_vs_targets = pd.merge(sales,targets)
print(sales_vs_targets)
crushing_it = sales_vs_targets[sales_vs_targets.revenue>sales_vs_targets.target]

import codecademylib
import pandas as pd
sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)
men_women = pd.read_csv('men_women_sales.csv')
all_data = sales.merge(targets).merge(men_women)
print(all_data)
results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]

import codecademylib
import pandas as pd
orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)
orders_products = pd.merge(orders,products.rename(columns = {'id':'product_id'}))
print(orders_products)

import codecademylib
import pandas as pd
orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)
orders_products = pd.merge(orders,products,left_on = 'product_id',right_on = 'id',suffixes = ['_orders','_products'])
print(orders_products)

import codecademylib
import pandas as pd
orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')
print(orders)
print(products)
merged_df = pd.merge(orders,products)
print(merged_df)

import codecademylib
import pandas as pd
store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)
store_a_b_outer = pd.merge(store_a,store_b,how='outer')
print(store_a_b_outer)

import codecademylib
import pandas as pd
store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)
store_a_b_left = pd.merge(store_a,store_b,how='left')
store_b_a_left = pd.merge(store_b,store_a,how='left')
print(store_a_b_left)
print(store_b_a_left)

import codecademylib
import pandas as pd
bakery = pd.read_csv('bakery.csv')
print(bakery)
ice_cream = pd.read_csv('ice_cream.csv')
print(ice_cream)
menu = pd.concat([bakery,ice_cream])
print(menu)

import codecademylib
import pandas as pd
visits = pd.read_csv('visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv',
                        parse_dates=[1])
print(visits)
print(checkouts)
v_to_c = pd.merge(visits,checkouts)
v_to_c['time'] = v_to_c.checkout_time - v_to_c.visit_time
print(v_to_c)
print(v_to_c.time.mean())
