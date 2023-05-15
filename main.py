import requests
from bs4 import BeautifulSoup as b

URL = "https://www.afisha.ru/tver/events/movies/"
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')  # Парсинг
    Text_for_films = soup.find_all('div', class_="mQ7Bh")
    return [c.text for c in Text_for_films]

Text_for_films = parser(URL)
Trach_words = ['События', 'Кино', 'Театр', 'Концерты', 'Дети', 'Об «Афише»', 'О нас', 'Проекты', 'Еще', '«Афиша» в соц. сетях', 'Мобильное приложение «Афиши» — самый удобный способ выбрать, как провести свободное время', 'Рассылка «Афиши»: главные события недели — у вас на почте']
def remove_common(Text_for_films, Trach_words):
    for i in Text_for_films[:]:
        if i in Trach_words:
            Text_for_films.remove(i)
            Trach_words.remove(i)

    print(Text_for_films)


c = remove_common(Text_for_films,Trach_words)
