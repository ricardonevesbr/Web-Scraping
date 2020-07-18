from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.aprendapowerbi.com.br/")
bsObj = BeautifulSoup(html.read(), "html.parser")

print(bsObj.find_all("h2"))