import requests
from bs4 import BeautifulSoup as b

URL = "https://www.afisha.ru/tver/events/movies/"
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')  # Парсинг
    Text_for_films = soup.find_all('div', class_="mQ7Bh")
    return [c.text for c in Text_for_films]

Text_for_films = parser(URL)
Test_spisok = ['Мама пошла в театр']
Trach_words = ['События', 'Кино', 'Театр', 'Концерты', 'Дети', 'Об «Афише»', 'О нас', 'Проекты', 'Еще', '«Афиша» в соц. сетях', 'Мобильное приложение «Афиши» — самый удобный способ выбрать, как провести свободное время', 'Рассылка «Афиши»: главные события недели — у вас на почте']

def remove_common(Test_spisok, Trach_words):
    for i in range(len(Test_spisok)):
        for j in range(len(Trach_words)):
            if j in Test_spisok:
                Test_spisok.remove(j)


print("list1 : ", Test_spisok)
print("list2 : ", Trach_words)

#def remove(Text_for_films, Trach_words):
    #r = []
    #for char in range(len(Text_for_films)):
        #if Text_for_films[char] != Trach_words[char]:
             #r.append(Text_for_films[char])
    #return r
#print(Text_for_films)