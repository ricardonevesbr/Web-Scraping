from scrapy import Selector
from urllib.request import urlopen


html = urlopen("https://www.pythonparatodos.com.br/formulario.html")
sel = Selector(text = html.read())
lista = sel.xpath('//input')
terceiro_input = lista[3]
print(terceiro_input.extract())
