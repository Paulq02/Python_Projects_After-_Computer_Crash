from bs4 import BeautifulSoup

import urllib.request, urllib.error, urllib.parse

link = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm").read()

soup = BeautifulSoup(link, "html.parser")

tags = soup("a")

for tag in tags:
    print(tag.get("href", None))


