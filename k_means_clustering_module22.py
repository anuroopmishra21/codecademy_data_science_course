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
