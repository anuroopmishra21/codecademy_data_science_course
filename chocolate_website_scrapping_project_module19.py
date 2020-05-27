import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
choc_raw = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html')
soup = BeautifulSoup(choc_raw.content,'html.parser')
print(soup)
rating = soup.find_all(attrs={'class':'Rating'})
print(rating)
ratings = []
for tag in rating[1:]:
  ratings.append(float(tag.get_text()))
plt.hist(ratings)
plt.show()
plt.clf()
company = soup.select('.Company')
company_name = []
for comp in company[1:]:
  company_name.append(comp.get_text())
d={'Company':company_name,'Ratings':ratings}
df = pd.DataFrame.from_dict(d)
average_ratings = df.groupby('Company').Ratings.mean()
ten_best=average_ratings.nlargest(10)
print(ten_best)
cocoa = soup.select('.CocoaPercent')
cocoa_percent = []
for cocoa in cocoa[1:]:
  cocoa_percent.append(int(float(cocoa.get_text().strip('%'))))
df['CocoaPercentage'] = cocoa_percent
plt.scatter(df.CocoaPercentage,df.Ratings)
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
plt.show()
