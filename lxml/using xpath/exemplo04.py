from lxml import html, etree
from urllib.request import urlopen

pagina = urlopen("https://www.pythonparatodos.com.br/formulario.html")
tree = html.fromstring(pagina.read())
tr = tree.xpath('//tr')
print(tr)
for elemento in tr:
    print(etree.tostring(elemento))