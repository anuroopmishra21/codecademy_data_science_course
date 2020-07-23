import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
digits = datasets.load_digits()
plt.gray()
plt.matshow(digits.images[100])
plt.show()
print(digits.target[100])
model = KMeans(n_clusters = 10)
model.fit(digits.data)
fig = plt.figure(figsize = (8,3))
fig.suptitle('Cluster Centre Images', fontsize = 14, fontweight = 'bold')
for i in range(10):
  ax = fig.add_subplot(2,5,1+i)
  ax.imshow(model.cluster_centers_[i].reshape((8,8)), cmap = plt.cm.binary)
plt.show()
new_samples = np.array([
[0.00,0.02,0.59,0.66,0.13,0.00,0.00,0.00,0.00,1.84,1.82,1.75,1.29,0.00,0.00,0.00,0.00,0.00,0.00,0.20,1.95,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.97,0.00,0.00,0.00,0.00,0.00,0.00,0.96,1.82,0.00,0.00,0.00,0.02,0.64,1.49,1.93,0.31,0.00,0.00,0.00,0.96,2.19,2.19,1.88,1.53,1.65,0.00,0.00,0.00,0.00,0.11,0.55,0.66,0.46,0.00,0.00],
[0.00,0.00,0.00,0.37,0.85,0.42,0.00,0.00,0.00,0.04,1.38,2.04,1.90,2.01,0.59,0.00,0.00,0.85,1.60,0.16,0.00,0.79,1.53,0.00,0.00,1.31,0.83,0.00,0.00,1.27,1.12,0.00,0.00,1.31,0.74,0.00,0.00,1.77,0.33,0.00,0.00,0.90,1.53,0.00,0.00,1.99,0.09,0.00,0.00,0.07,1.84,1.53,1.43,1.99,0.00,0.00,0.00,0.00,0.18,0.81,1.01,0.20,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.07,1.49,1.97,1.97,1.91,0.90,0.00,0.00,0.24,1.20,0.24,0.22,0.57,1.75,0.00,0.00,0.00,0.00,0.00,0.00,0.55,1.71,0.00,0.00,0.00,0.00,0.04,0.77,1.97,0.72,0.00,0.00,0.00,0.33,1.73,2.08,1.19,0.72,0.86,0.00,0.00,1.16,1.75,1.75,1.60,1.53,1.01,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.02,0.75,0.00,0.00,0.00,0.00,0.00,0.00,0.57,2.19,0.61,0.00,0.00,0.00,0.00,0.00,1.62,1.95,0.98,0.00,0.00,0.00,0.00,0.18,1.99,0.70,1.51,0.00,0.00,0.00,0.00,0.02,0.44,0.31,1.82,0.00,0.00,0.00,0.00,0.00,0.00,0.02,1.99,0.00,0.00,0.00,0.00,0.00,0.00,0.00,2.03,0.11,0.00,0.00,0.00,0.00,0.00,0.00,0.99,0.09,0.00,0.00]
])
new_labels = model.predict(new_samples)
for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')
