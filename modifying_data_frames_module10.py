import codecademylib
import pandas as pd
df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)
df['Sold in Bulk?'] = ['Yes','Yes','No','No']
print(df)

import codecademylib
import pandas as pd
df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)
df['Is taxed?'] = 'Yes'
print(df)

import codecademylib
import pandas as pd
df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)
df['Margin'] = df['Price'] - df['Cost to Manufacture']
print(df)

import codecademylib
from string import lower
import pandas as pd
df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])
df['Lowercase Name'] = df.Name.apply(lower)
print(df)

mylambda = lambda x: x[0]+x[-1]
print(mylambda('hello world'))

mylambda = lambda x: 'Welcome to BattleCity!' if x >= 13 else 'You must be over 13'
print(mylambda(14))

import codecademylib
import pandas as pd
df = pd.read_csv('employees.csv')
get_last_name = lambda x:x.split(' ')[-1]
df['last_name'] = df.name.apply(get_last_name)
print(df)
