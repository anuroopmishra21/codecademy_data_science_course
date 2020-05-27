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
