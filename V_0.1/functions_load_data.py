from bs4 import BeautifulSoup
import copy
from dict_structures import data_season, data_episode

def get_int(text):
    for t in text.split():
        try:
            number= (int(t))
        except ValueError:
            pass
    return number

def load_basic_data(serie_basic_info, data, cant_season):
    data['title'] = serie_basic_info.find('h1', attrs={"class":"title-title"}).text
    data['year']= int(serie_basic_info.find('span', attrs={"class":"title-info-metadata-item item-year"}).text)
    data['maturity-rating'] = serie_basic_info.find('span', attrs={"class":"maturity-number"}).text.replace(" ", "")
    data['synopsis']= serie_basic_info.find('div', attrs={"class": "title-info-synopsis"}).text
    data['directed']= serie_basic_info.find('span', attrs={"class":"title-data-info-item-list"}).text
    data['seasons']= cant_season

def load_episodes_data(episodes):
    all_episodes=[]
    index=1
    for episode in episodes:
        data_e = copy.deepcopy(data_episode)
        data_e['number']= index
        data_e['title']= episode.find('h3', attrs={"class": "episode-title"}).text.split(".")[1]
        data_e['duration']= get_int(episode.find('span', attrs={"class":"episode-runtime"}).text)
        data_e['synopsis']= episode.find('p', attrs={"class":"epsiode-synopsis"}).text
        all_episodes.append(data_e)
        index+=1
    return all_episodes

def load_season_data(series_season):
    seasons=[]
    index=1

    for season in series_season:
        data_s = copy.deepcopy(data_season)
        data_s['number']= index
        data_s['year']= get_int(season.find('div',{"class":"season-release-year"}).text)
        data_s['synopsis']= season.find('p', attrs={"class":"season-synopsis"}).text
        data_s['episodes']= load_episodes_data( season.find_all('div', attrs={"class":"episode"}) )
        seasons.append(data_s)
        index+=1
    return seasons

def load_specific_data(data_serie, serie_info):
    serie_genres = serie_info.find_all('a', attrs={"class": "more-details-item item-genres"})
    genres=[]
    for genre in serie_genres:
        genres.append(genre.text)
    data_serie['genres']=genres
    starring_list= serie_info.find_all('span', attrs={"class": "more-details-item item-cast"})
    starring=[]
    for starr in starring_list:
        starring.append(starr.text)
    data_serie['starring']=starring 