from matplotlib import pyplot as plt

import codecademylib
from matplotlib import pyplot as plt
days = [0,1,2,3,4,5,6]
money_spent = [10,12,12,10,14,22,24]
plt.plot(days,money_spent)
plt.show()

import codecademylib
from matplotlib import pyplot as plt
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]
plt.plot(time,revenue)
plt.plot(time,costs)
plt.show()

import codecademylib
from matplotlib import pyplot as plt
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]
plt.plot(time,revenue,color = 'purple',linestyle = '--')
plt.plot(time,costs,color = '#82edc9',marker = 's')
plt.show()

import codecademylib
from matplotlib import pyplot as plt
x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)
plt.axis([0,12,2900,3100])
plt.show()

import codecademylib
from matplotlib import pyplot as plt

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)
plt.axis([0, 12, 2900, 3100])
plt.xlabel('Time')
plt.ylabel('Dollars spent on coffee')
plt.title('My Last Twelve Years of Coffee Drinking')
plt.show()

import codecademylib
from matplotlib import pyplot as plt
months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]
plt.subplot(1,2,1)
plt.plot(temperature,months)
plt.subplot(1,2,2)
plt.plot(temperature,flights_to_hawaii,marker = 'o')
plt.show()

import codecademylib
from matplotlib import pyplot as plt
x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]
plt.subplot(2,1,1)
plt.plot(x,straight_line)
plt.subplot(2,2,3)
plt.plot(x,parabola)
plt.subplot(2,2,4)
plt.plot(x,cubic)
plt.subplots_adjust(wspace = 0.35,bottom = 0.2)
plt.show()

import codecademylib
from matplotlib import pyplot as plt
months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]
plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)
legend_labels=['Hyrule','Kakariko','Gerudo Valley']
plt.legend(legend_labels,loc=8)
plt.show()

import codecademylib
from matplotlib import pyplot as plt
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]
months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]
plt.xlabel("Months")
plt.ylabel("Conversion")
plt.plot(months, conversion)
ax=plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.set_yticks([0.10,0.25,0.5,0.75])
ax.set_yticklabels(['10%','25%','50%','75%'])
plt.show()

import codecademylib
from matplotlib import pyplot as plt
word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
plt.close('all')
plt.figure()
plt.plot(years,word_length)
plt.savefig('winning_word_lengths.png')
plt.figure(figsize = (7,3))
plt.plot(years,power_generated)
plt.savefig('power_generated.png')
plt.show()

import codecademylib
from matplotlib import pyplot as plt
x=[1,2,3,4,5]
y1=[720,768,923,892,911]
y2=[766,987,709,897,953]
plt.plot(x,y1,color='pink',marker='o')
plt.plot(x,y2,color='gray',marker='o')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
plt.title('Two Lines on One Graph')
plt.legend(['y1','y2'],loc=4)
plt.axis([1,5,720,987])
plt.show()
