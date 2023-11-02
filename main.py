import requests
import bs4

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, 'html.parser')
movies = soup.find_all(class_= 'listicleItem_listicle-item__title__hW_Kn')
i = 1
for movie in movies:
    all_movies = movie.text.split(') ')
    print(f'{i}) {all_movies[1]}')
    i += 1