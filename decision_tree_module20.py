from tree import tree, classify
car = ['med','med','4','more','big','high']
print(classify(car,tree))

from collections import Counter
labels = ["unacc", "unacc", "acc", "acc", "good", "good"]
#labels = ["unacc","unacc","unacc", "good", "vgood", "vgood"]
#labels = ["unacc", "unacc", "unacc", "unacc", "unacc", "unacc"]
impurity = 1
label_counts = Counter(labels)
print(label_counts)
for label in label_counts:
  probability_of_label = label_counts[label]/len(labels)
  impurity -= probability_of_label**2
print(impurity)

from collections import Counter
unsplit_labels = ["unacc", "unacc", "unacc", "unacc", "unacc", "unacc", "good", "good", "good", "good", "vgood", "vgood", "vgood"]
split_labels_1 = [
  ["unacc", "unacc", "unacc", "unacc", "unacc", "unacc", "good", "good", "vgood"], 
  [ "good", "good"], 
  ["vgood", "vgood"]
]
split_labels_2 = [
  ["unacc", "unacc", "unacc", "unacc","unacc", "unacc", "good", "good", "good", "good"], 
  ["vgood", "vgood", "vgood"]
]
def gini(dataset):
  impurity = 1
  label_counts = Counter(dataset)
  for label in label_counts:
    prob_of_label = label_counts[label] / len(dataset)
    impurity -= prob_of_label ** 2
  return impurity
info_gain = gini(unsplit_labels)
for subset in split_labels_2:
  info_gain -= gini(subset)
print(info_gain)

from collections import Counter
cars = [['med', 'low', '3', '4', 'med', 'med'], ['med', 'vhigh', '4', 'more', 'small', 'high'], ['high', 'med', '3', '2', 'med', 'low'], ['med', 'low', '4', '4', 'med', 'low'], ['med', 'low', '5more', '2', 'big', 'med'], ['med', 'med', '2', 'more', 'big', 'high'], ['med', 'med', '2', 'more', 'med', 'med'], ['vhigh', 'vhigh', '2', '2', 'med', 'low'], ['high', 'med', '4', '2', 'big', 'low'], ['low', 'low', '2', '4', 'big', 'med']]
car_labels = ['acc', 'acc', 'unacc', 'unacc', 'unacc', 'vgood', 'acc', 'unacc', 'unacc', 'good']
def split(dataset, labels, column):
    data_subsets = []
    label_subsets = []
    counts = list(set([data[column] for data in dataset]))
    counts.sort()
    for k in counts:
        new_data_subset = []
        new_label_subset = []
        for i in range(len(dataset)):
            if dataset[i][column] == k:
                new_data_subset.append(dataset[i])
                new_label_subset.append(labels[i])
        data_subsets.append(new_data_subset)
        label_subsets.append(new_label_subset)
    return data_subsets, label_subsets
def gini(dataset):
  impurity = 1
  label_counts = Counter(dataset)
  for label in label_counts:
    prob_of_label = label_counts[label] / len(dataset)
    impurity -= prob_of_label ** 2
  return impurity
def information_gain(starting_labels, split_labels):
  info_gain = gini(starting_labels)
  for subset in split_labels:
    # Multiply gini(subset) by the correct percentage below
    info_gain -= (len(subset)/len(starting_labels))*gini(subset)
  return info_gain
for i in range(6):
  split_data, split_labels = split(cars,car_labels,i)
  print(information_gain(car_labels,split_labels))

from tree import *
car_data = [['med', 'low', '3', '4', 'med', 'med'], ['med', 'vhigh', '4', 'more', 'small', 'high'], ['high', 'med', '3', '2', 'med', 'low'], ['med', 'low', '4', '4', 'med', 'low'], ['med', 'low', '5more', '2', 'big', 'med'], ['med', 'med', '2', 'more', 'big', 'high'], ['med', 'med', '2', 'more', 'med', 'med'], ['vhigh', 'vhigh', '2', '2', 'med', 'low'], ['high', 'med', '4', '2', 'big', 'low'], ['low', 'low', '2', '4', 'big', 'med']]
car_labels = ['acc', 'acc', 'unacc', 'unacc', 'unacc', 'vgood', 'acc', 'unacc', 'unacc', 'good']
def find_best_split(dataset, labels):
    best_gain = 0
    best_feature = 0
    for feature in range(len(dataset[0])):
        data_subsets, label_subsets = split(dataset, labels, feature)
        gain = information_gain(labels, label_subsets)
        if gain > best_gain:
            best_gain, best_feature = gain, feature
    return best_feature, best_gain
def build_tree(data,labels):
  best_feature, best_gain = find_best_split(data,labels)
  if best_gain == 0:
    return Counter(labels)
  data_subsets, label_subsets = split(data,labels,best_feature)
  branches = []
  for i in range(len(data_subsets)):
    branches.append(build_tree(data_subsets[i],label_subsets[i]))
  return branches
tree = build_tree(car_data,car_labels)
print_tree(tree)

from tree import *
import operator
test_point = ['vhigh', 'low', '3', '4', 'med', 'med']
def classify(datapoint,tree):
  if isinstance(tree, Leaf):
    return max(tree.labels.items(), key=operator.itemgetter(1))[0]
  value = datapoint[tree.feature]
  for branch in tree.branches:
    if branch.value == value:
      return classify(datapoint, branch)
print(classify(test_point,tree))

from cars import training_points, training_labels, testing_points, testing_labels
from sklearn.tree import DecisionTreeClassifier
print(training_points[0],training_labels[0])
classifier = DecisionTreeClassifier()
classifier.fit(training_points,training_labels)
print(classifier.score(testing_points,testing_labels))

from cars import training_points, training_labels, testing_points, testing_labels
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(random_state = 0, max_depth = 11)
classifier.fit(training_points, training_labels)
print(classifier.score(testing_points, testing_labels))
print(classifier.tree_.max_depth)
