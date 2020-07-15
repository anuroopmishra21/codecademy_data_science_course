import codecademylib3_seaborn
import numpy as np
import matplotlib.pyplot as plt
from exam import hours_studied, passed_exam, math_courses_taken
plt.scatter(hours_studied.ravel(), passed_exam, color='black', zorder=20)
plt.ylabel('passed/failed')
plt.xlabel('hours studied')
plt.show()

mport codecademylib3_seaborn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from exam import hours_studied, passed_exam
from plotter import plot_data
model = LinearRegression()
model.fit(hours_studied,passed_exam)
sample_x = np.linspace(-16.65, 33.35, 300).reshape(-1,1)
probability = model.predict(sample_x).ravel()
plot_data(model)
plt.show()
slacker = -0.1
studious = 1.1

import codecademylib3_seaborn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from exam import hours_studied, passed_exam
from plotter import plot_data
model = LogisticRegression()
model.fit(hours_studied,passed_exam)
sample_x = np.linspace(-16.65, 33.35, 300).reshape(-1,1)
probability = model.predict_proba(sample_x)[:,1]
plot_data(model)
plt.show()
lowest = 0
highest = 1

import numpy as np
from exam import hours_studied, calculated_coefficients, intercept
# Create your log_odds() function here
def log_odds(features, coefficients, intercept):
  return (np.dot(features,coefficients) + intercept)
# Calculate the log-odds for the Codecademy University data here
calculated_log_odds = log_odds(hours_studied, calculated_coefficients, intercept)
print(calculated_log_odds)

import codecademylib3_seaborn
import numpy as np
from exam import calculated_log_odds
def sigmoid(z):
  denominator = 1 + np.exp(-z)
  return 1/denominator
probabilities  = sigmoid(calculated_log_odds)
print(probabilities)

import numpy as np
from exam import passed_exam, probabilities, probabilities_2
def log_loss(probabilities,actual_class):
  return np.sum(-(1/actual_class.shape[0])*(actual_class*np.log(probabilities) + (1-actual_class)*np.log(1-probabilities)))
# Print passed_exam here
print(passed_exam)
# Calculate and print loss_1 here
loss_1 = log_loss(probabilities,passed_exam)
print(loss_1)
# Calculate and print loss_2 here
loss_2 = log_loss(probabilities_2,passed_exam)
print(loss_2)
