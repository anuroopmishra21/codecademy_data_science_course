dataset_one = [50, 10, 4, -3, 4, -20, 2]
sorted_dataset_one = [-20, -3, 2, 4, 4, 10, 50]
dataset_two = [24, 20, 1, 45, -15, 40]
sorted_dataset_two = [-15, 1, 20, 24, 40, 45]
#Define the second quartile of both datasets here:
dataset_one_q2 = 4
dataset_two_q2 = (20+24)/2
#Ignore the code below here:
try:
  print("The second quartile of dataset one is " + str(dataset_one_q2))
except NameError:
  print("You haven't defined dataset_one_q2")
try:
  print("The second quartile of dataset two is " + str(dataset_two_q2))
except NameError:
  print("You haven't defined dataset_two_q2")
  
dataset_one = [50, 10, 4, -3, 4, -20, 2]
sorted_dataset_one =  [-20,-3, 2, 4, 4, 10, 50]
dataset_two = [24, 20, 1, 45, -15, 40]
sorted_dataset_two = [-15, 1, 20, 24, 40, 45]
sorted_dataset_two
dataset_one_q2 = 4
dataset_two_q2 = 22
dataset_one_q1 = -3
dataset_one_q3 = 10
dataset_two_q1 = 1
dataset_two_q3 = 40
#Ignore the code below here:
try:
  print("The first quartile of dataset one is " + str(dataset_one_q1))
except NameError:
  print("You haven't defined dataset_one_q1")
try:
  print("The second quartile of dataset one is " + str(dataset_one_q2))
except NameError:
  print("You haven't defined dataset_one_q2")
try:
  print("The third quartile of dataset one is " + str(dataset_one_q3) + "\n")
except NameError:
  print("You haven't defined dataset_one_q3\n")
try:
  print("The first quartile of dataset two is " + str(dataset_two_q1))
except NameError:
  print("You haven't defined dataset_two_q1")
try:
  print("The second quartile of dataset two is " + str(dataset_two_q2))
except NameError:
  print("You haven't defined dataset_two_q2")
try:
  print("The third quartile of dataset two is " + str(dataset_two_q3))
except NameError:
  print("You haven't defined dataset_two_q3")

dataset_one = [50, 10, 4, -3, 4, -20, 2]
sorted_dataset_one = [-20, -3, 2, 4, 4, 10, 50]
dataset_two = [24, 20, 1, 45, -15, 40]
sorted_dataset_two = [-15, 1, 20, 24, 40, 45] 
dataset_one_q2 = 4
dataset_two_q2 = 22
#Define the first and third quartile of both datasets here:
dataset_one_q1 = -0.5
dataset_one_q3 = 7
dataset_two_q1 = 1
dataset_two_q3 = 40
#Ignore the code below here:
try:
  print("The first quartile of dataset one is " + str(dataset_one_q1))
except NameError:
  print("You haven't defined dataset_one_q1")
try:
  print("The second quartile of dataset one is " + str(dataset_one_q2))
except NameError:
  print("You haven't defined dataset_one_q2")
try:
  print("The third quartile of dataset one is " + str(dataset_one_q3) + "\n")
except NameError:
  print("You haven't defined dataset_one_q3\n")
try:
  print("The first quartile of dataset two is " + str(dataset_two_q1))
except NameError:
  print("You haven't defined dataset_two_q1")
try:
  print("The second quartile of dataset two is " + str(dataset_two_q2))
except NameError:
  print("You haven't defined dataset_two_q2")
try:
  print("The third quartile of dataset two is " + str(dataset_two_q3))
except NameError:
  print("You haven't defined dataset_two_q3")

from song_data import songs
import numpy as np
#Create the variables songs_q1, songs_q2, and songs_q3 here:
songs_q1 = np.quantile(songs,0.25)
songs_q2 = np.quantile(songs,0.5)
songs_q3 = np.quantile(songs,0.75)
favorite_song = 261
quarter = 3
#Ignore the code below here:
try:
  print("The first quartile of dataset one is " + str(songs_q1) + " seconds")
except NameError:
  print("You haven't defined songs_q1")
try:
  print("The second quartile of dataset one is " + str(songs_q2)+ " seconds")
except NameError:
  print("You haven't defined songs_q2")
try:
  print("The third quartile of dataset one is " + str(songs_q3)+ " seconds")
except NameError:
  print("You haven't defined songs_q3\n")
