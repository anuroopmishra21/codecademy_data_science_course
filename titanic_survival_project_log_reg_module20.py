import codecademylib3_seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
passengers = pd.read_csv("passengers.csv")
passengers['Sex'] = passengers['Sex'].map({'male':'0','female':'1'})
passengers['Age'].fillna(value = passengers['Age'].mean(),inplace = True)
passengers['FirstClass'] = passengers['Pclass'].apply(lambda x: 1 if x==1 else 0)
passengers['SecondClass'] = passengers['Pclass'].apply(lambda x: 1 if x==2 else 0)
print(passengers)
features = passengers[['Sex','Age','FirstClass','SecondClass']]
survival = passengers['Survived']
train_set,test_set,train_labels,test_labels = train_test_split(features,survival,test_size = 0.2)
scaler = StandardScaler()
train_set = scaler.fit_transform(train_set)
test_set = scaler.transform(test_set)
model = LogisticRegression()
model.fit(train_set,train_labels)
print(model.score(train_set,train_labels))
print(model.score(test_set,test_labels))
print(model.coef_)
Jack = np.array([0.0,20.0,0.0,0.0])
Rose = np.array([1.0,17.0,1.0,0.0])
You = np.array([0.0,20.0,1.0,0.0])
sample_passengers = np.array([Jack,Rose,You])
sample_passengers = scaler.transform(sample_passengers)
print(sample_passengers)
print(model.predict(sample_passengers))
print(model.predict_proba(sample_passengers))
