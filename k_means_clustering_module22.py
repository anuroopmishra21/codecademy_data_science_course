import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np 
from os.path import join, dirname, abspath
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn import datasets
iris = datasets.load_iris()
x = iris.data
y = iris.target
fignum = 1
# Plot the ground truthd
fig = plt.figure(fignum, figsize=(4, 3))
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
for name, label in [('Zombies', 0),
                    ('Programmers', 1),
                    ('Vampires', 2)]:
    ax.text3D(x[y == label, 3].mean(),
              x[y == label, 0].mean(),
              x[y == label, 2].mean() + 2, name,
              horizontalalignment='center',
              bbox=dict(alpha=.2, edgecolor='w', facecolor='w'))
# Reorder the labels to have colors matching the cluster results
y = np.choose(y, [1, 2, 0]).astype(np.float)
ax.scatter(x[:, 3], x[:, 0], x[:, 2], c=y, edgecolor='k')
ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])
ax.set_xlabel('hates sunlight')
ax.set_ylabel('likes garlic')
ax.set_zlabel('canine teeth (in)')
ax.set_title('')
ax.dist = 12
# Add code here:
plt.show()

import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn import datasets
iris = datasets.load_iris()
print(iris.data)
print(iris.target)
print(iris.DESCR)

import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn import datasets
iris = datasets.load_iris()
# Store iris.data
samples = iris.data
# Create x and y
x = samples[:,0]
y = samples[:,1]
# Plot x and y
plt.scatter(x,y,alpha = 0.5)
# Show the plot
plt.show()

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
iris = datasets.load_iris()
samples = iris.data
x = samples[:,0]
y = samples[:,1]
# Number of clusters
k = 3
# Create x coordinates of k random centroids
centroids_x = np.random.uniform(min(x), max(x), 3)
# Create y coordinates of k random centroids
centroids_y = np.random.uniform(min(y), max(y), 3)
# Create centroids array
centroids = np.array(list(zip(centroids_x, centroids_y)))
print(centroids)
# Make a scatter plot of x, y
plt.scatter(x , y, alpha =0.5)
# Make a scatter plot of the centroids
plt.scatter(centroids_x, centroids_y)
# Display plot
plt.show()

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
iris = datasets.load_iris()
samples = iris.data
x = samples[:,0]
y = samples[:,1]
sepal_length_width = np.array(list(zip(x, y)))
# Step 1: Place K random centroids
k = 3
centroids_x = np.random.uniform(min(x), max(x), size=k)
centroids_y = np.random.uniform(min(y), max(y), size=k)
centroids = np.array(list(zip(centroids_x, centroids_y)))
# Step 2: Assign samples to nearest centroid
def distance(a,b):
  distance = 0
  for i in range(len(a)):
    distance += (a[i]-b[i])**2
  return distance**0.5
labels = np.zeros(len(samples))
distances = np.zeros(k)
for i in range(len(samples)):
  for j in range(k):
    distances[j] = distance(sepal_length_width[i], centroids[j])
  cluster = np.argmin(distances)
  labels[i] = cluster
print(labels)

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from copy import deepcopy
iris = datasets.load_iris()
samples = iris.data
samples = iris.data
x = samples[:,0]
y = samples[:,1]
sepal_length_width = np.array(list(zip(x, y)))
# Step 1: Place K random centroid
k = 3
centroids_x = np.random.uniform(min(x), max(x), size=k)
centroids_y = np.random.uniform(min(y), max(y), size=k)
centroids = np.array(list(zip(centroids_x, centroids_y)))
# Step 2: Assign samples to nearest centroid
def distance(a, b):
  one = (a[0] - b[0]) **2
  two = (a[1] - b[1]) **2
  distance = (one+two) ** 0.5
  return distance
# Cluster labels for each point (either 0, 1, or 2)
labels = np.zeros(len(samples))
# Distances to each centroid
distances = np.zeros(k)
for i in range(len(samples)):
  distances[0] = distance(sepal_length_width[i], centroids[0])
  distances[1] = distance(sepal_length_width[i], centroids[1])
  distances[2] = distance(sepal_length_width[i], centroids[2])
  cluster = np.argmin(distances)
  labels[i] = cluster
# Step 3: Update centroids
centroids_old = deepcopy(centroids)
for i in range(k):
  points = []
  for j in range(len(sepal_length_width)):
    if labels[j] == i:
      points.append(sepal_length_width[j])
  centroids[i] = np.mean(points, axis =0)
print(centroids_old)
print(centroids)

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from copy import deepcopy
iris = datasets.load_iris()
samples = iris.data
x = samples[:,0]
y = samples[:,1]
sepal_length_width = np.array(list(zip(x, y)))
# Step 1: Place K random centroids
k = 3
centroids_x = np.random.uniform(min(x), max(x), size=k)
centroids_y = np.random.uniform(min(y), max(y), size=k)
centroids = np.array(list(zip(centroids_x, centroids_y)))
def distance(a, b):
  one = (a[0] - b[0]) ** 2
  two = (a[1] - b[1]) ** 2
  distance = (one + two) ** 0.5
  return distance
# To store the value of centroids when it updates
centroids_old = np.zeros(centroids.shape)
# Cluster labeles (either 0, 1, or 2)
labels = np.zeros(len(samples))
distances = np.zeros(3)
# Initialize error:
error = np.zeros(3)
error[0] = distance(centroids[0], centroids_old[0])
error[1] = distance(centroids[1], centroids_old[1])
error[2] = distance(centroids[2], centroids_old[2])
# Repeat Steps 2 and 3 until convergence:
while error.all() != 0:
  # Step 2: Assign samples to nearest centroid
  for i in range(len(samples)):
    distances[0] = distance(sepal_length_width[i], centroids[0])
    distances[1] = distance(sepal_length_width[i], centroids[1])
    distances[2] = distance(sepal_length_width[i], centroids[2])
    cluster = np.argmin(distances)
    labels[i] = cluster
  # Step 3: Update centroids
  centroids_old = deepcopy(centroids)
  for i in range(3):
    points = [sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j] == i]
    centroids[i] = np.mean(points, axis=0)
  error[0] = distance(centroids[0], centroids_old[0])
  error[1] = distance(centroids[1],   centroids_old[1])
  error[2] = distance(centroids[2], centroids_old[2])
colors = ['r', 'g', 'b']
for i in range(k):
  points = np.array([sepal_length_width[j] for j in range(len(samples)) if labels[j] == i])
  plt.scatter(points[:, 0], points[:, 1], c=colors[i], alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='D', s=150)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()

import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
iris = datasets.load_iris()
samples = iris.data
model = KMeans(n_clusters = 3)
model.fit(samples)
labels = model.predict(samples)
print(labels)

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans
iris = datasets.load_iris()
samples = iris.data
model = KMeans(n_clusters=3)
model.fit(samples)
new_samples = np.array([[5.7, 4.4, 1.5, 0.4],
   [6.5, 3. , 5.5, 0.4],
   [5.8, 2.7, 5.1, 1.9]])
print(new_samples)
print(model.predict(new_samples))

import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
iris = datasets.load_iris()
samples = iris.data
model = KMeans(n_clusters=3)
model.fit(samples)
labels = model.predict(samples)
print(labels)
x = samples[:,0]
y = samples[:,1]
plt.scatter(x, y, c = labels, alpha = 0.5)
plt.xlabel("Sepal Length in cm")
plt.ylabel("Sepal width in cm")
plt.show()

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd
iris = datasets.load_iris()
samples = iris.data
target = iris.target
model = KMeans(n_clusters=3)
model.fit(samples)
labels = model.predict(samples)
species = np.chararray(target.shape, itemsize=150)
for i in range(len(samples)):
  if target[i] == 0:
    species[i] = 'setosa'
  elif target[i] == 1:
    species[i] = 'versicolor'
  elif target[i] == 2: 
    species[i] = 'virginica'
df = pd.DataFrame({'labels': labels, 'species': species})
print(df)
ct = pd.crosstab(df['labels'], df['species'])
print(ct)

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans
iris = datasets.load_iris()
samples = iris.data
num_clusters = list(range(1,9))
inertias = []
for i in num_clusters:
  model = KMeans(n_clusters = i)
  model.fit(samples)
  inertias.append(model.inertia_)
plt.plot(num_clusters, inertias, '-o')
plt.xlabel('Number of Clusters(k)')
plt.ylabel('Inertia')
plt.show()
