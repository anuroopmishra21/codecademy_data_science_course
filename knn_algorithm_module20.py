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
