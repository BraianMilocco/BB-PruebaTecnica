import requests
from bs4 import BeautifulSoup
import json
import sys

#Funciones de carga de datos
from functions_load_data import getBasicData, getSeasonData
#info
from info import info, error, ayuda

if len(sys.argv) == 1:
    print(error)
    sys.exit()
if sys.argv[1] == "--series":
    print(info)
    sys.exit()
if sys.argv[1] == "--ayuda":
    print(ayuda)
    sys.exit()
if not sys.argv[1].isnumeric():
    print(error)
    exit()
    

#Armado de URL Se separan los campos por si se quisiera pasar el id por parámetro
#O con alguna estructura auxiliar para reutilizar el código con múltiples series
basic_url= 'https://www.netflix.com/ar/title/'
series_id=  sys.argv[1]
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

#Carga la información basica de la serie, titulo, cantidad de temporada.. 
data_serie= getBasicData(
    serie_basic_info, 
    len(series_season), 
    series_specific_info)

#Carga la información relacionada a las temporadas y capítulos
data_serie['seasons-data']= [getSeasonData(season, index) 
    for index, season in enumerate(series_season)
    ]


json_object= json.dumps(data_serie, indent=4, ensure_ascii=False)

print (json_object)
