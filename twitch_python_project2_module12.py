import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# Bar Graph: Featured Games
games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]
viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]
plt.bar(range(len(games)),viewers,color='green')
ax=plt.subplot()
ax.set_xticks(range(len(games)))
ax.set_xticklabels(games,rotation=60)
plt.title('Viewers for games')
plt.xlabel('Games')
plt.ylabel('Viewers')
plt.legend('Twitch')
plt.show()
plt.clf()
# Pie Chart: League of Legends Viewers' Whereabouts
labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]
countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]
colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
plt.pie(countries,explode=explode,shadow=True,startangle=345,autopct='%1.0f%%',pctdistance=1.15,colors=colors)
plt.axis('equal')
plt.title('League of Legends Viewers Whereabouts')
plt.legend(labels,loc='right')
plt.show()
plt.clf()
# Line Graph: Time Series Analysis
hour = range(24)
viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]
y_lower=[i*0.85 for i in viewers_hour]
y_upper=[i*1.15 for i in viewers_hour]
plt.plot(hour,viewers_hour)
ax=plt.subplot()
ax.set_xticks(hour)
plt.xlabel('Hours')
plt.ylabel('Viewers')
plt.title('Viewers each hour')
plt.fill_between(hour,y_lower,y_upper,alpha=0.3)
plt.show()
