import codecademylib
import pandas as pd
ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())
view_count = ad_clicks.groupby('utm_source').user_id.count().reset_index()
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
).reset_index()
print(clicks_pivot)
clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True]+clicks_pivot[False])
a_or_b = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(a_or_b)
clicks_by_group = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()
clicks_by_group_pivot = clicks_by_group.pivot(
  columns = 'is_click',
  index = 'experimental_group',
  values = 'user_id'
).reset_index()
print(clicks_by_group_pivot)
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
a_percent = a_clicks.groupby(['day','is_click']).user_id.count().reset_index()
a_percent_pivot = a_percent.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()
b_percent = b_clicks.groupby(['day','is_click']).user_id.count().reset_index()
b_percent_pivot = b_percent.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()
print(a_percent_pivot)
print(b_percent_pivot)
