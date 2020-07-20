from tree import build_tree, print_tree, car_data, car_labels
import random
random.seed(4)
tree = build_tree(car_data,car_labels)
#print_tree(tree)
indices = [random.randint(0,999) for i in range(1000)]
data_subset =[car_data[index] for index in indices]
labels_subset = [car_labels[index] for index in indices]
subset_tree = build_tree(data_subset, labels_subset)
print_tree(subset_tree)

from tree import car_data, car_labels, split, information_gain
import random
import numpy as np
np.random.seed(1)
random.seed(4)
def find_best_split(dataset, labels):
    best_gain = 0
    best_feature = 0
    #Create features here
    features = np.random.choice(len(dataset[0]), 3, replace = False)
    for feature in features:
        data_subsets, label_subsets = split(dataset, labels, feature)
        gain = information_gain(labels, label_subsets)
        if gain > best_gain:
            best_gain, best_feature = gain, feature
    return best_gain, best_feature
indices = [random.randint(0, 999) for i in range(1000)]
data_subset = [car_data[index] for index in indices]
labels_subset = [car_labels[index] for index in indices]
print(find_best_split(data_subset, labels_subset))

from tree import build_tree, print_tree, car_data, car_labels, classify
import random
random.seed(4)
# The features are the price of the car, the cost of maintenance, the number of doors, the number of people the car can hold, the size of the trunk, and the safety rating
unlabeled_point = ['high', 'vhigh', '3', 'more', 'med', 'med']
predictions = []
for i in range(20):
  indices = [random.randint(0, 999) for i in range(1000)]
  data_subset = [car_data[index] for index in indices]
  labels_subset = [car_labels[index] for index in indices]
  subset_tree = build_tree(data_subset, labels_subset)
  predictions.append(classify(unlabeled_point, subset_tree))
print(predictions)
final_prediction = max(predictions, key=predictions.count)
print(final_prediction)

from tree import training_data, training_labels, testing_data, testing_labels, make_random_forest, make_single_tree, classify
import numpy as np
import random
np.random.seed(1)
random.seed(1)
tree = make_single_tree(training_data, training_labels)
forest = make_random_forest(40, training_data, training_labels)
forest_correct = 0
single_tree_correct = 0
for i in range(len(testing_data)):
  prediction = classify(testing_data[i], tree)
  if prediction == testing_labels[i]:
    single_tree_correct += 1
  predictions = []
  for forest_tree in forest:
    predictions.append(classify(testing_data[i], forest_tree))
  forest_prediction = max(predictions,key=predictions.count)
  if forest_prediction == testing_labels[i]:
    forest_correct +=1
print(single_tree_correct/len(testing_data))
print(forest_correct/len(testing_data))

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
from cars import training_points, training_labels, testing_points, testing_labels
import warnings
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 2000, random_state = 0)
classifier.fit(training_points, training_labels)
print(classifier.score(testing_points, testing_labels))
