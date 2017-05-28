#importing everything we need
import sqlite3
import requests
from bs4 import BeautifulSoup

#class for working with our SQL-DataBase
class SQLHelper:
    name = 'Examination.db'

    _db_connection = None
    _db_cur = None

    def __init__(self):
        self._db_connection = sqlite3.connect(self.name)
        self._db_cur = self._db_connection.cursor()

    def query(self, query):
        self._db_cur.execute(query)
        self._db_connection.commit()

    def fetch(self, query):
        return self._db_cur.execute(query).fetchall()

    def save(self):
        self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()

#class for saving information about products on https://www.re-store.ru/apple-mac/
class Computer:
    article = ''
    title = ''
    price = ''

    def __init__(self, article, title, price):
        self.article = article
        self.title = title
        self.price = price

#preparing for parsing
db = SQLHelper()
url = "https://www.re-store.ru/apple-mac/"
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, "lxml")
info = soup.find("div", {"class" : "w-4-fifth last"}).findAll("div", {"class" : "product-item__main"})
print(info)

#in 'computers' we will save computer-class objects
computers = []

#parse!
for item in info:
    #taking out everything we need
    articles = item.find("p", {"class": "product-item__article"})
    titles = item.find("p", {"class" : "product-item__title"})
    prices = item.find("span", {"class" : "product-item__price"}).find("span", {"class" : "product-item__price__num"})

    #append parsed information to 'computers' by computer-class object
    computers.append(Computer(articles.text, titles.text, prices.text))

#putting information in SQL-Database
for a in computers:
    try:
        db.query(("INSERT INTO Apple(article, title, price) VALUES ('%s', '%s', '%s');") % (a.article, a.title, a.price))
        db.save()
    except TypeError:
        pass
