import requests
from bs4 import BeautifulSoup
import json

#Funciones de carga de datos
from functions_load_data import load_basic_data, load_season_data, load_specific_data
#Diccionarios donde cargar la información
from dict_structures  import data_serie

#Armado de URL Se separan los campos por si se quisiera pasar el id por parámetro
#O con alguna estructura auxiliar para reutilizar el código con múltiples series
basic_url= 'https://www.netflix.com/ar/title/'
series_id=  '70143836'
url= basic_url + series_id





#Se recibe la información de la url
page_response = requests.get(url, timeout=5)
#Se parse a html la informaión recibida
page_content = BeautifulSoup(page_response.content, "html.parser")

#Se separa la información básica de la Serie (title, year, maturity, synopsis, directed, seasons)
serie_basic_info = page_content.find('div',attrs={"class":"title-info"})

#Se separa información mas completa de la Serie (Genres, Starring, specific-tags)
series_specific_info= page_content.find('section', attrs={"id":"section-more-details"})

#Se separa la información de las temporadas y capítulos
series_season = page_content.find_all('div', attrs={"class":"season"})


load_basic_data(serie_basic_info, data_serie, len(series_season))

seasons= load_season_data(series_season)

data_serie['seasons-data']= seasons

load_specific_data(data_serie, series_specific_info)

json_object= json.dumps(data_serie, indent=4)

print (json_object)