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
