value = 7

width=5
ans=2

import codecademylib
import numpy as np
from matplotlib import pyplot as plt
commutes = np.genfromtxt('commutes.csv', delimiter=',')
plt.hist(commutes,range = (20,50),bins = 6)
plt.show()

graph_a = "multimodal"
graph_b = "unimodal"
graph_c = "bimodal"

graph_a = 'skew-right'
graph_b = 'skew-left'
graph_c = 'symmetric'

import codecademylib
import numpy as np
from matplotlib import pyplot as plt
# Brachiosaurus
b_data = np.random.normal(6.7,0.7,size=1000)
# Fictionosaurus
f_data = np.random.normal(7.7,0.3,size=1000)
plt.hist(b_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Brachiosaurus')
plt.hist(f_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Fictionosaurus')
plt.xlabel('Femur Length (ft)')
plt.legend(loc=2)
plt.show()
mystery_dino = 'Brachiosaurus'
answer = False

import numpy as np
one_above = 1100
one_below = 900
print(one_above)
print(one_below)
one_std = 1360
print(one_std)

import codecademylib
import numpy as np
from matplotlib import pyplot as plt
emails = np.random.binomial(500,0.05,size=10000)
plt.hist(emails)
plt.show()

import numpy as np
emails = np.random.binomial(500, 0.05, size=10000)
no_emails = np.mean(emails == 0)
b_test_emails = np.mean(emails == 0.08)
print(no_emails)
print(b_test_emails)

import codecademylib
import numpy as np
from matplotlib import pyplot as plt
sunflowers = np.genfromtxt('sunflower_heights.csv', delimiter=',')
sunflowers_mean = np.mean(sunflowers)
sunflowers_std = np.std(sunflowers)
sunflowers_normal = np.random.normal(sunflowers_mean,sunflowers_std,size=5000)
plt.hist(sunflowers,
         range=(11, 15), histtype='step', linewidth=2,
        label='observed', normed=True)
plt.hist(sunflowers_normal,
         range=(11, 15), histtype='step', linewidth=2,
        label='normal', normed=True)
plt.legend()
plt.show()
experiments = np.random.binomial(200,0.1,5000)
prob = np.mean(experiments < 20)
print(prob)
