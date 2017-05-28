import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://www.re-store.ru/apple-mac/"
html_doc = requests.get(url).text
# print(html_doc)
soup = BeautifulSoup(html_doc, "lxml")


class DB:
    path = ''

    _db_connection = None
    _db_cur = None

    def __init__(self, path):
        self.path = path
        self._db_connection = sqlite3.connect(self.path)
        self._db_cur = self._db_connection.cursor()

    def query(self, query):
        return self._db_cur.execute(query)

    def fetch(self, query):
        return self._db_cur.execute(query).fetchall()

    def save(self):
        self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()


class computer:
    article = ''
    characteristics = ''
    price = ''
    presence = ''
    name = ''

    def __init__(self, article, characteristics, price, presence, name):
        self.article = article
        self.characteristics = characteristics
        self.price = price
        self.presence = presence
        self.name = name

info = soup.find("div", {"class" : "w-4-fifth last"}).findAll("p")

for item in info:
    article = ''

