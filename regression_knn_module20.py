from movies import movie_dataset, movie_ratings
def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance
def predict(unknown, dataset, movie_ratings, k):
  distances = []
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    distances.append([distance_to_point, title])
  distances.sort()
  neighbors = distances[0:k]
  sum = 0
  for movie in neighbors:
    title = movie[1]
    sum += movie_ratings[title]
  return round((sum/k),2)
print(predict([0.016,0.300,1.022],movie_dataset,movie_ratings,5))

from movies import movie_dataset, movie_ratings
def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance
def predict(unknown, dataset, movie_ratings, k):
  distances = []
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    distances.append([distance_to_point, title])
  distances.sort()
  neighbors = distances[0:k]
  numerator = 0
  denominator = 0
  for movie in neighbors:
    title = movie[1]
    numerator += (movie_ratings[title]/movie[0])
    denominator += (1/movie[0])
  return numerator/denominator
print(predict([0.016,0.300,1.022],movie_dataset,movie_ratings,5))

