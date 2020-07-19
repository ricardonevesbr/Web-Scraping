from scrapy import Selector
from urllib.request import urlopen


html = urlopen("https://www.pythonparatodos.com.br/formulario.html")
sel = Selector(text = html.read())
lista = sel.xpath('//input[@type="text"]')
print(lista)
for selector in lista:
    print(selector)