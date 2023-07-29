from bs4 import BeautifulSoup

f_handle = open("index.html")

soup = BeautifulSoup(f_handle, "html.parser")

tags = soup.find_all("a")

link_list = []
for link in tags:
    link = link.get("href", None)
    link_list.append(link)

print(link_list)
    
    
  








