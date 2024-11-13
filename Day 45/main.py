from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_webpage = response.text
soup = BeautifulSoup(empire_webpage, "html.parser")

movies = [film.getText() for film in soup.find_all(name="h3", class_="title")]
movies.reverse()
# print(movies[58])
movies[58] = "59) E.T. The Extra Terrestrial"
print(movies)
with open("movies.txt", mode="w") as file:
     for movie in movies:
         file.write(f"{movie}\n")
