mean_girls = [97, 17000000, False]
the_shining = [146, 19000000, True]
gone_with_the_wind = [238, 3977000, False]

star_wars = [125, 1977]
raiders = [115, 1981]
mean_girls = [97, 2004]
def distance(movie1, movie2):
  d=0
  for i in range(len(movie1)):
    d += (movie1[i]-movie2[i])**2
  return d**0.5
print(distance(star_wars,raiders))
print(distance(star_wars,mean_girls))

star_wars = [125, 1977, 11000000]
raiders = [115, 1981, 18000000]
mean_girls = [97, 2004, 17000000]
def distance(movie1, movie2):
  d=0
  for i in range(len(movie1)):
    d+=(movie1[i]-movie2[i])**2
  return d**0.5
print(distance(star_wars,raiders))
print(distance(star_wars,mean_girls))

release_dates = [1897, 1998, 2000, 1948, 1962, 1950, 1975, 1960, 2017, 1937, 1968, 1996, 1944, 1891, 1995, 1948, 2011, 1965, 1891, 1978]
def min_max_normalize(lst):
  minimum = min(lst)
  maximum = max(lst)
  normalized = []
  for i in lst:
    val = (i-minimum)/(maximum-minimum)
    normalized.append(val)
  return normalized
print(min_max_normalize(release_dates))

from movies import movie_dataset, movie_labels
print(movie_dataset['Bruce Almighty'])
print(movie_labels['Bruce Almighty'])
def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance
def classify(unknown,dataset,k):
  distances =[]
  for title in dataset:
    distance_to_point = distance(dataset[title],unknown)
    distances.append([distance_to_point,title])
    distances.sort()
    neighbors = distances[:k]
  return neighbors
print(classify([.4,.2,.9],movie_dataset,5))

from movies import movie_dataset, movie_labels
def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance
def classify(unknown, dataset, labels, k):
  distances = []
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    distances.append([distance_to_point, title])
  distances.sort()
  neighbors = distances[0:k]
  num_good = 0
  num_bad = 0
  for movie in neighbors:
    title = movie[1]
    if labels[title] == 0:
      num_bad+=1
    else:
      num_good+=1
  if num_good>num_bad:
    return 1
  else:
    return 0
print(classify([.4,.2,.9],movie_dataset,movie_labels,5))

from movies import movie_dataset, movie_labels, normalize_point
def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance
def classify(unknown, dataset, labels, k):
  distances = []
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    distances.append([distance_to_point, title])
  distances.sort()
  neighbors = distances[0:k]
  num_good = 0
  num_bad = 0
  for neighbor in neighbors:
    title = neighbor[1]
    if labels[title] == 0:
      num_bad += 1
    elif labels[title] == 1:
      num_good += 1
  if num_good > num_bad:
    return 1
  else:
    return 0
my_movie = [350000,132,2017]
normalized_my_movie = normalize_point(my_movie)
print(normalized_my_movie)
print(classify(normalized_my_movie,movie_dataset,movie_labels,5))

from movies import training_set, training_labels, validation_set, validation_labels
def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance
def classify(unknown, dataset, labels, k):
  distances = []
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    distances.append([distance_to_point, title])
  distances.sort()
  neighbors = distances[0:k]
  num_good = 0
  num_bad = 0
  for neighbor in neighbors:
    title = neighbor[1]
    if labels[title] == 0:
      num_bad += 1
    elif labels[title] == 1:
      num_good += 1
  if num_good > num_bad:
    return 1
  else:
    return 0
print(validation_set['Bee Movie'])
print(validation_labels['Bee Movie'])
guess = classify(validation_set['Bee Movie'],training_set,training_labels,5)
print(guess)
print('Correct!')

from movies import training_set, training_labels, validation_set, validation_labels
def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance
def classify(unknown, dataset, labels, k):
  distances = []
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    distances.append([distance_to_point, title])
  distances.sort()
  neighbors = distances[0:k]
  num_good = 0
  num_bad = 0
  for neighbor in neighbors:
    title = neighbor[1]
    if labels[title] == 0:
      num_bad += 1
    elif labels[title] == 1:
      num_good += 1
  if num_good > num_bad:
    return 1
  else:
    return 0
def find_validation_accuracy(training_set,training_labels,validation_set,validation_labels,k):
  num_correct = 0.0
  for movie in validation_set:
    guess = classify(validation_set[movie],training_set,training_labels,k)
    if guess == validation_labels[movie]:
      num_correct+=1
  validation_error = num_correct/len(validation_set)
  return validation_error
print(find_validation_accuracy(training_set,training_labels,validation_set,validation_labels,3))

from movies import movie_dataset, labels
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(movie_dataset,labels)
print(classifier.predict([[.45,.2,.5],[.25,.8,.9],[.1,.1,.9]]))

