import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz
def svc(player):
  player['type'] = player['type'].map({'S':1 , 'B':0})
  player = player.dropna(subset = ['plate_x','plate_z','type'])
  fig, ax = plt.subplots()
  plt.scatter(x=player.plate_x,y=player.plate_z,c=player.type,cmap = plt.cm.coolwarm , alpha = 0.25)
  training_set,validation_set = train_test_split(player,random_state = 1)
  classifier = SVC(kernel = 'rbf', gamma = 3, C=1)
  classifier.fit(training_set[['plate_x','plate_z']],training_set['type'])
  draw_boundary(ax,classifier)
  print(classifier.score(validation_set[['plate_x','plate_z']],validation_set['type']))
  ax.set_ylim(-2,6)
  ax.set_xlim(-3,3)
  plt.show()
svc(jose_altuve)
