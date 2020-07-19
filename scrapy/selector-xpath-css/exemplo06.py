from scrapy import Selector
from urllib.request import urlopen


html = urlopen("https://www.pythonparatodos.com.br/formulario.html")
sel = Selector(text = html.read())
lista = sel.css('tr:nth-of-type(2)')
for x in lista:
    print(x)
