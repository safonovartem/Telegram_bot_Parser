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
a = Text_for_films
b = Trach_words
print(a)
print(b)
def remove_common(a, b):
    for i in a[:]:
        if i in b:
            a.remove(i)
            b.remove(i)
    print("list1 : ", a)
    print("list2 : ", b)


c = remove_common(a,b)
