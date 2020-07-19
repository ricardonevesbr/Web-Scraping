from scrapy import Selector
from urllib.request import urlopen


html = urlopen("https://www.pythonparatodos.com.br/formulario.html")
sel = Selector(text = html.read())
lista = sel.css('html > body > form > table > tr')
for x in lista:
    print(x)
