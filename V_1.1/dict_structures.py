#Estructuras base Diccionarios donde cargar la información

data_serie={
    'title': None,
    'year': None,
    'maturity-rating': None,
    'genres': None,
    'synopsis': None,
    'starring': None,
    'directed': None,
    'seasons': None,
    'seasons-data':[], #Data_season List
    }

data_season= {
    'number': None,
    'year': None,
    'synopsis': None,
    'episodes':[], #data_episode List
}

data_episode= {
    'number': None,
    'title': None,
    'duration': None,
    'synopsis': None,
}