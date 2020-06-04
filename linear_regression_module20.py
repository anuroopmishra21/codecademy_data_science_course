import codecademylib3_seaborn
import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]
#slope:
m = 12
#intercept:
b = 40
y = [m*i + b for i in months]
plt.plot(months, revenue, "o")
plt.plot(months,y)
plt.show()

x = [1, 2, 3]
y = [5, 1, 3]
#y = x
m1 = 1
b1 = 0
y_predicted1 = [m1*x+b1 for x in x]
#y = 0.5x + 1
m2 = 0.5
b2 = 1
y_predicted2 = [m2*x+b2 for x in x]
total_loss1 = 0
for i in range(len(y)):
  total_loss1 +=(y[i]-y_predicted1[i])**2
total_loss2 = 0
for i in range(len(y)):
  total_loss2 +=(y[i]-y_predicted2[i])**2
print(total_loss1,total_loss2)
better_fit = 2

def get_gradient_at_b(x,y,m,b):
  diff = 0
  for i in range(len(x)):
    diff+=y[i]-(m*x[i]+b)
  b_gradient = -2/(len(x))*diff
  return b_gradient

def get_gradient_at_b(x, y, m, b):
    diff = 0
    N = len(x)
    for i in range(N):
      y_val = y[i]
      x_val = x[i]
      diff += (y_val - ((m * x_val) + b))
    b_gradient = -2/N * diff
    return b_gradient
def get_gradient_at_m(x, y, m, b):
    diff = 0
    N = len(x)
    for i in range(N):
      y_val = y[i]
      x_val = x[i]
      diff += x_val*(y_val - ((m * x_val) + b))
    m_gradient = -2/N * diff
    return m_gradient
  
 def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient
def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient
def step_gradient(x,y,b_current,m_current):
  b_gradient = get_gradient_at_b(x,y,b_current,m_current)
  m_gradient = get_gradient_at_m(x,y,b_current,m_current)
  b = b_current - (0.01 * b_gradient)
  m = m_current - (0.01 * b_gradient)
  return [b,m]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]
b = 0
m = 0
b, m = step_gradient(months, revenue, b, m)
print(b, m)

import codecademylib3_seaborn
import matplotlib.pyplot as plt
from data import bs, bs_000000001, bs_01
iterations = range(1400)
plt.plot(iterations, bs)
plt.xlabel("Iterations")
plt.ylabel("b value")
plt.show()
num_iterations = 800
convergence_b = 47

import codecademylib3_seaborn
import matplotlib.pyplot as plt
from data import bs, bs_000000001, bs_01
iterations = range(100)
plt.plot(iterations, bs_01)
plt.xlabel("Iterations")
plt.ylabel("b value")
plt.show()
num_iterations = 800
convergence_b = 47

import codecademylib3_seaborn
import matplotlib.pyplot as plt
def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient
def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient
def step_gradient(b_current, m_current, x, y,learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]
def gradient_descent(x,y,learning_rate,num_iterations):
  b=0
  m=0
  for i in range(num_iterations):
    b,m=step_gradient(b,m,x,y,learning_rate)
  return b,m
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]
b, m = gradient_descent(months, revenue, 0.01, 1000)
y = [m*x + b for x in months]
plt.plot(months, revenue, "o")
plt.plot(months, y)
plt.show()import codecademylib3_seaborn
import matplotlib.pyplot as plt
def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient
def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient
def step_gradient(b_current, m_current, x, y,learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]
def gradient_descent(x,y,learning_rate,num_iterations):
  b=0
  m=0
  for i in range(num_iterations):
    b,m=step_gradient(b,m,x,y,learning_rate)
  return b,m
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]
b, m = gradient_descent(months, revenue, 0.01, 1000)
y = [m*x + b for x in months]
plt.plot(months, revenue, "o")
plt.plot(months, y)
plt.show()

import codecademylib3_seaborn
from gradient_descent_funcs import gradient_descent
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("heights.csv")
X = df["height"]
y = df["weight"]
b,m = gradient_descent(X,y,0.0001,1000)
y_predictions = [m*x + b for x in X]
plt.plot(X, y, 'o')
#plot your line here:
plt.plot(X,y_predictions)
plt.show()

import codecademylib3_seaborn
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
temperature = np.array(range(60, 100, 2))
temperature = temperature.reshape(-1, 1)
sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]
line_fitter = LinearRegression()
line_fitter.fit(temperature,sales)
sales_predict = line_fitter.predict(temperature)
plt.plot(temperature, sales, 'o')
plt.plot(temperature,sales_predict)
plt.show()
