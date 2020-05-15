import pandas as pd
from matplotlib import pyplot as plt
restaurants=pd.read_csv('restaurants.csv')
print(restaurants.head())
cuisine_options_count=restaurants.cuisine.nunique()
cuisine_counts=restaurants.groupby('cuisine').name.count().reset_index()
print(cuisine_options_count)
print(cuisine_counts)
