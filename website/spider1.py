import requests
import urllib2
from bs4 import BeautifulSoup

# specify the url
team_page="https://www.thebluealliance.com/teams"
page=urllib2.urlopen(team_page)

#parse the html using beautiful soup 
soup = BeautifulSoup(page,'html.parser')

nameBox=soup.find('h1',attr={'class':'name'})
name= nameBox.text.strip()
print(name)
numberBox=soup.find('div',attr={'class':"container"})
number=numberBox.text
print(number)