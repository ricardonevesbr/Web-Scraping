from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://localhost:8000")
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.html.tag_nao_existente.outra_tag)