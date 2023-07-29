"""import urllib.request, urllib.error, urllib.parse

link = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

for line in link:
    print(line.decode().strip())"""

from bs4 import BeautifulSoup

f_handle = open("index.html")

soup = BeautifulSoup(f_handle, "html.parser")

tags = soup("a")
for tag in tags:
    print(tag.get("href", None))

