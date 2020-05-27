from preprocess import turtles
print(turtles)

respect = 'I will not spam websites'

import requests
webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')
webpage = webpage_response.content
print(webpage)

import requests
from bs4 import BeautifulSoup
webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')
webpage = webpage_response.content
soup = BeautifulSoup(webpage,'html.parser')
print(soup)

import requests
from bs4 import BeautifulSoup
webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
print(soup.p)
print(soup.p.string)

import requests
from bs4 import BeautifulSoup
webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
for child in soup.div.children:
  print(child)

import requests
from bs4 import BeautifulSoup
webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
turtle_links = soup.find_all('a')
print(turtle_links)

import requests
from bs4 import BeautifulSoup
prefix = "https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/"
webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them:
for a in turtle_links:
  links.append(prefix+a["href"])
#Define turtle_data:
turtle_data = {}
#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  turtle_name = turtle.select(".name")[0]
  turtle_data[turtle_name] = []
print(turtle_data)

import requests
from bs4 import BeautifulSoup
prefix = "https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/"
webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them:
for a in turtle_links:
  links.append(prefix+a["href"])
#Define turtle_data:
turtle_data = {}
#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  turtle_name = turtle.select(".name")[0]
  turtle_data[turtle_name.get_text()] = turtle.find('ul').get_text('|').split('|')
print(turtle_data)

import requests
from bs4 import BeautifulSoup
import pandas as pd
prefix = "https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/"
webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them"
for a in turtle_links:
  links.append(prefix+a["href"])
#Define turtle_data:
turtle_data = {}
#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  turtle_name = turtle.select(".name")[0].get_text()
  stats = turtle.find("ul")
  stats_text = stats.get_text("|")
  turtle_data[turtle_name] = stats_text.split("|")
turtle_df = pd.DataFrame.from_dict(turtle_data,orient = 'index')
