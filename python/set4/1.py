from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://example.webscraping.com/places/default/index"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
type(soup)
#************************************
print("Country Names    :")
for div in soup.findAll('td'):
    fileName = div.findNext('a').text
    print(fileName)
    
#***********************************    
print("images URL :")
all_imgs = soup.find_all("img")
for imgs in all_imgs:
    print(imgs.get("src"))
    print(imgs.get_text())
