import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from graph import ax, x_1, y_1, x_2, y_2
#Top graph intercept and slope
intercept_one = 8
slope_one = -2
x_vals = np.array(ax.get_xlim())
y_vals = intercept_one + slope_one * x_vals
plt.plot(x_vals, y_vals, '-')
#Bottom Graph
ax = plt.subplot(2, 1, 2)
plt.title('Good Decision Boundary')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
plt.scatter(x_1, y_1, color = "b")
plt.scatter(x_2, y_2, color = "r")
#Change the intercept to separate the clusters
intercept_two = 14
slope_two = -2
x_vals = np.array(ax.get_xlim())
y_vals = intercept_two + slope_two * x_vals
plt.plot(x_vals, y_vals, '-')
plt.tight_layout()
plt.show()

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from graph import ax, x_1, y_1, x_2, y_2
#Top graph intercept and slope
intercept_one = 98
slope_one = -20
x_vals = np.array(ax.get_xlim())
y_vals = intercept_one + slope_one * x_vals
plt.plot(x_vals, y_vals, '-')
#Bottom graph
ax = plt.subplot(2, 1, 2)
plt.title('Good Decision Boundary')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
plt.scatter(x_1, y_1, color = "b")
plt.scatter(x_2, y_2, color = "r")
intercept_two = 8
slope_two = -0.5
x_vals = np.array(ax.get_xlim())
y_vals = intercept_two + slope_two * x_vals
plt.plot(x_vals, y_vals, '-')
plt.tight_layout()
plt.show()

red_support_vector = [1,6]
blue_support_vector_one = [0.5, 2]
blue_support_vector_two = [2.5, 2]
margin_size = 2

from sklearn.svm import SVC
from graph import points, labels
classifier = SVC(kernel = "linear")
classifier.fit(points,labels)
print(classifier.predict([[3,4],[6,7]]))

import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from graph import points, labels, draw_points, draw_margin
points.append([3,3])
labels.append(0)
points.append([1,11])
labels.append(1)
points.append([5,9])
labels.append(1)
classifier = SVC(kernel='linear', C = 0.2)
classifier.fit(points, labels)
draw_points(points, labels)
draw_margin(classifier)
plt.show()
