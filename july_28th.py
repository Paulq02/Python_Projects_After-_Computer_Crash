import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

link = urllib.request.urlopen("http://books.toscrape.com/catalogue/category/books/science_22/index.html")

soup = BeautifulSoup(link, "html.parser")



print(soup)

