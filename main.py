import requests
from bs4 import BeautifulSoup as b

URL = 'https://www.afisha.ru/tver/events/na-segodnya/'
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')#Парсинг
    Text_for_films = soup.find_all('div', class_ = "mQ7Bh")
    return [c.text for c in Text_for_films]

list_of_jokes = parser(URL)
print(list_of_jokes)
#list_of_jokes = len(list_of_jokes)
#print(list_of_jokes)
del list_of_jokes[8]#Надо придумать как подчистить список
#Clean_list_of_jokes =

print(list_of_jokes)

