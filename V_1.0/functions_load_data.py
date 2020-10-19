from bs4 import BeautifulSoup
import copy
from dict_structures import data_serie, data_season, data_episode

def get_int(text):
    for t in text.split():
        try:
            number= (int(t))
        except ValueError:
            pass
    return number

def getEpisodeData(episode, index):
    data_e = copy.deepcopy(data_episode)
    
    data_e['number']= index + 1
    data_e['title']= episode.find('h3', attrs={"class": "episode-title"}).text.split(".")[1]
    data_e['duration']= get_int(episode.find('span', attrs={"class":"episode-runtime"}).text)
    data_e['synopsis']= episode.find('p', attrs={"class":"epsiode-synopsis"}).text

    return data_e

def getSeasonData(season, index):
    data_s = copy.deepcopy(data_season)

    data_s['number']= index +1
    data_s['year']= get_int(season.find('div',{"class":"season-release-year"}).text)
    data_s['synopsis']= season.find('p', attrs={"class":"season-synopsis"}).text
    
    data_s['episodes']=[ getEpisodeData(episode, index) 
        for index, episode in enumerate(season.find_all('div', attrs={"class":"episode"}))
        ] 

    return data_s


def getBasicData(serie_basic_info, cant_season, complete_genres_casting):
    data= copy.deepcopy(data_serie)
    
    #Info from serie_basic_info
    data['title'] = serie_basic_info.find('h1', attrs={"class":"title-title"}).text
    data['year']= int(serie_basic_info.find('span', attrs={"class":"title-info-metadata-item item-year"}).text)
    data['maturity-rating'] = serie_basic_info.find('span', attrs={"class":"maturity-number"}).text.replace(" ", "")
    data['synopsis']= serie_basic_info.find('div', attrs={"class": "title-info-synopsis"}).text
    data['directed']= serie_basic_info.find('span', attrs={"class":"title-data-info-item-list"}).text

    data['seasons']= cant_season

    #Info from complete_genres_casting
    data['genres']= [genre.text 
        for genre in complete_genres_casting('a', attrs={"class": "more-details-item item-genres"})
        ]
    data['starring']= [starring.text
        for starring in complete_genres_casting.find_all('span', attrs={"class": "more-details-item item-cast"})
        ]

    return data