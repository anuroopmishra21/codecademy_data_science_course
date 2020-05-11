import codecademylib
import pandas as pd
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ['t-shirt','t-shirt','skirt','skirt'],
  'Color':['blue','green','red','black']
})
print(df1)

import codecademylib
import pandas as pd
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3,'San Francisco',90],
  [4,'Sacramento',115]
],
  columns=[
    'Store ID','Location','Number of Employees'
  ])
print(df2)
