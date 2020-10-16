import requests
from bs4 import BeautifulSoup
import json

url= 'https://www.netflix.com/ar/title/70143836'

data={}

page_response = requests.get(url, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")

detalle = page_content.find('div',attrs={"class":"title-info"})

#title= page_content.find('h1', attrs={"class":"title-title"}).text
title = detalle.find('h1').text

temporadas= page_content.find_all('div', attrs={"class":"season"})

data["title"]= detalle.find('h1',attrs={"class":"title-title"}).text
data["maturity-rating"]= detalle.find('span', attrs={"class":"maturity-number"}).text.replace(" ", "")

print(data)