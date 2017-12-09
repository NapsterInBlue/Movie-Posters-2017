import requests
import re
from bs4 import BeautifulSoup

def process_data(imgTag):
    title = clean_title(imgTag.get('alt'))
    download_image(imgTag, title)
    genres = {title: get_genres(imgTag)}
    return genres


def clean_title(title):
    cleanChars = re.compile('[A-Z0-9 ]', re.I)
    title = ''.join(re.findall(cleanChars, title))
    return title

def download_image(imgTag, title):
    url = imgTag.get('data-original')
    if not url:
        url = imgTag.get('src')

    if url:
        image = requests.get(url).content

        f = open('posters/'+title+'.png', 'wb')
        f.write(image)
        f.close()

def get_genres(imgTag):
    base = 'http://www.wildaboutmovies.com'
    url = base + imgTag.parent.get('href')

    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    metaData = soup.find_all('div', {'class':'meta'})
    try:
        genreLine = list(filter(lambda x: x.text.startswith('Genre'), metaData))[0]
    except:
        print(imgTag.get('alt'), "didn't have a genre")
        return

    if genreLine.text.startswith('Genres:'):
        genres = [x.text for x in list(genreLine.children)[1:]]
        return genres
    else:
        print("Genres isn't the second line")