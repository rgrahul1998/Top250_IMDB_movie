import requests
from bs4 import *
import pandas as pd

try:
    request = requests.get("https://www.imdb.com/chart/top")
    print(request)
    request.raise_for_status()

    soup = BeautifulSoup(request.text, 'html.parser')
    # print(soup)

    movies = soup.find('tbody', class_='lister-list')
    movies = movies.find_all('tr')
    # print(movies)

    name_list = []
    year_list = []
    rank_list = []
    rating_list = []

    for movie in movies:

        name = movie.find('td', class_='titleColumn')
        name = name.a.text
        name_list.append(name)

        # print(name)

        year = movie.find('span', class_='secondaryInfo')
        year = year.text
        year = year.strip('()')
        year_list.append(year)
        # print(year)

        rank = movie.find('td', class_='titleColumn')
        rank = rank.get_text(strip=True)
        rank = rank.split('.')
        rank = rank[0]
        rank_list.append(rank)
        # print(rank)

        rating = movie.find('td', class_='ratingColumn imdbRating')
        rating = rating.strong.text
        rating_list.append(rating)
        # print(rating)

    # print (rank_list)
    # print(name_list)
    # print(year_list)
    # print(rating_list)

    dic = {"rank":rank_list, "name":name_list, "year":year_list, "rating":rating_list}

    df = pd.DataFrame(dic)
    # print(df)

    df.to_excel('IMDB_rating.xlsx', index=False)

except Exception as e:
    print(e)

print ('Excel file is ready')
