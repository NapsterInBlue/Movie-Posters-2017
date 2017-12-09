import pickle

import requests
from bs4 import BeautifulSoup

from processdata import process_data

url = r'http://www.wildaboutmovies.com/2017_movies/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml').find('div', {'id':'content'})

posters = [a.find('img') for a in soup.find_all('a') if a.find('img')]

genres = {}

for poster in posters:
    genre = process_data(poster)
    genres = {**genres, **genre}

f = open('genres.pkl', 'wb')
pickle.dump(genres, f)
f.close()