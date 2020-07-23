import codecademylib3_seaborn
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from copy import deepcopy
from sklearn.cluster import KMeans 
x = [1, 1, 4, 4]
y = [1, 3, 1, 3]
values = np.array(list(zip(x, y)))
centroids_x = [2.5, 2.5]
centroids_y = [1, 3]
centroids = np.array(list(zip(centroids_x, centroids_y)))
model = KMeans(init='k-means++', n_clusters=2)
results = model.fit_predict(values)
plt.scatter(x, y, c=results, alpha=1)
# Cluster centers
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], marker='v', s=100)
ax = plt.subplot()
ax.set_xticks([0, 1, 2, 3, 4, 5])
ax.set_yticks([0, 1, 2, 3, 4])
plt.title('K-Means++ Initialization')
plt.show()
print("The model's inertia is " + str(model.inertia_))
