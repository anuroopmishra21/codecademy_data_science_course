import codecademylib3_seaborn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
flags = pd.read_csv('flags.csv', header = 0)
labels = flags['Landmass']
data = flags[["Red", "Green", "Blue", "Gold",
 "White", "Black", "Orange",
 "Circles",
"Crosses","Saltires","Quarters","Sunstars",
"Crescent","Triangle"]]
train_data,test_data,train_labels,test_labels = train_test_split(data, labels, random_state = 1)
scores=[]
for i in range(1,21):
  classifier = DecisionTreeClassifier(random_state = 1, max_depth = i)
  classifier.fit(train_data,train_labels)
  scores.append(classifier.score(test_data,test_labels))
plt.plot(range(1,21),scores)
plt.show()
